''' Root class '''

from golftracker import media_pipe_landmarks
from golftracker import ml_pose_operation as ml_op
from golftracker import golf_poses
from golftracker import golf_handedness
from golftracker import club_head_detection as ch_op
from golftracker import gt_const as gt
from golftracker import geom
from golftracker import video_utils

import cv2
from collections import namedtuple

VideoInput = namedtuple("VideoInput", ['fname', 'size', 'scale', 'rotate'])

class GolfSwing:
    def __init__(self, height, width, num_frames, fps, video_input):
        self.height = height
        self.width = width
        self.num_frames = num_frames
        self.fps = fps
        self.video_input = video_input

        # Lazy eval for frames.
        self.frames = []

        # Init media pipe operation
        self.mp_results = media_pipe_landmarks.MediaPipeLandmarks(num_frames)

        # ML model for pose detection
        self.pose_results = [gt.GolfPose.Unknown] * num_frames
        self.pose_sequence = (None, None)  # Start to end pose frames
        self.handed = gt.Handedness.Unknown  # Is it left or right handed.
        
    def load_hints(self, hints_fname):
        self.params.load_hints(hints_fname)

    # Get frames from video lazily
    def get_video_frames(self):
        if not self.frames:
            (self.frames, _) = video_utils.split_video_to_frames(
                    self.video_input.fname, scale=self.video_input.scale, 
                    rotate=self.video_input.rotate)
        return self.frames


    # Media pipe interface
    # norm_points: are normalized coordinates on the screen.
    # screen_points: are screen coordinates with upper left as origin.

    def set_mp_landmarks(self, video_landmarks):
        """Store the landmarks in a flat row. """
        self.mp_results.set_mp_results(video_landmarks)

    def get_mp_landmarks_flat_row(self, frame_idx):
        return self.mp_results.get_mp_landmarks_flat_row(frame_idx)

    def get_mp_norm_points_dict(self, frame_idx):
        """Return a dictwith x, y coordinates of media pipe landmarks on frame.
        The keys are defined in gt_const.MP_POSE_LANDMARKS.
        For ex: {'nose': [0.4, 0.3], 'left_eye_inner': [0.45, 0.3], ....}
        """
        return self.mp_results.get_norm_points_dict(frame_idx)

    def get_mp_norm_point(self, frame_idx, pt_name):
        return self.mp_results.get_norm_point(frame_idx, pt_name)

    def get_mp_norm_point_path(self, pt_name):
        """Return a list of (x, y) norm coord of the point in entire video"""
        return [
            self.mp_results.get_mp_norm_point(idx, pt_name) 
                    for idx in range(self.num_frames)
        ]


    # ML model for pose detection.
    # Find the pose detected on a frame.
    #
    def classify_golf_poses(self, pose_model):
        """ Run pose model on each frame and store the poses. """
        for frame_idx in range(self.num_frames):
            row = self.mp_results.get_mp_landmarks_flat_row(frame_idx)
            pose = ml_op.run(pose_model, row, gt.ML_POSE_PROB_THRESHOLD)
            self.pose_results[frame_idx] = pose

    def get_golf_pose(self, frame_idx):
        """ Return the golf pose enum type for the frame.
            If no pose detected then return state Unknown.
        """
        return self.pose_results[frame_idx]

    # Pose sequence
    # Find the golf swing by looking at the correct sequence of poses.
    # 
    def find_golf_swing_sequence(self):
        """Run the golf swing sequencer to detect the subset of frames with swing."""
        starting_frame = golf_poses.get_pose_first_start(self.pose_results)
        ending_frame = golf_poses.get_pose_last_finish(self.pose_results)
        self.pose_sequence = (starting_frame, ending_frame)
        self.handed = golf_handedness.run([])

   
    def is_valid_swing(self):
        """
        Return true if we detected a valid swing.
        """
        status = False
        if self.pose_sequence[0] is not None and self.pose_sequence[1] is not None:
            num_swing_frames = self.pose_sequence[1] - self.pose_sequence[0]
            if num_swing_frames > 5:  # Arbitary
                status = True

        return status
    
    #
    # Visualize golf swing.
    # 
    def draw_frame(self, frame_idx, background_frame):
        # Draw media pipe
        self.mp_results.draw_frame(frame_idx, background_frame)

        (h, w, _) = background_frame.shape
        # Draw a line from the hand to the club head.
        club_head_point = self.computed_club_head_points[frame_idx]
        if club_head_point:
            (norm_x, norm_y) = club_head_point
            (x1, y1) = (int(norm_x * w), int(norm_y * h))
            mp_data = self.get_mp_points(frame_idx, h, w)
            (x2, y2) = mp_data["right_thumb"]
            cv2.line(background_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    