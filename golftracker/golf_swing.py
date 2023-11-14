''' Root class '''

from golftracker import media_pipe_landmarks
from golftracker import pose_result
from golftracker import club_head_result
from golftracker import video_utils
from golftracker import image_utils

from collections import namedtuple
import cv2

VideoInput = namedtuple("VideoInput", ['fname', 'size', 'scale', 'rotate'])
VideoSpec = namedtuple("VideoSpec", ['height', 'width', 'num_frames', 'fps'])

class GolfSwing:
    def __init__(self, video_spec, video_input):
        self.height = video_spec.height
        self.width = video_spec.width
        self.num_frames = video_spec.num_frames
        self.fps = video_spec.fps
        self.video_input = video_input

        # Lazy eval for frames.
        self.frames = []

        # Results
        self.mp_result = media_pipe_landmarks.MediaPipeLandmarks(self.num_frames)
        self.pose_result = pose_result.PoseResult(self.num_frames)
        self.club_head_result = club_head_result.ClubHeadResult(self.num_frames)

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
        self.mp_result.set_video_landmarks(video_landmarks)

    def get_mp_landmarks_flat_row(self, frame_idx):
        return self.mp_result.get_mp_landmarks_flat_row(frame_idx)

    def get_mp_norm_points_dict(self, frame_idx):
        """Return a dictwith x, y coordinates of media pipe landmarks on frame.
        The keys are defined in gt_const.MP_POSE_LANDMARKS.
        For ex: {'nose': [0.4, 0.3], 'left_eye_inner': [0.45, 0.3], ....}
        """
        return self.mp_result.get_norm_points_dict(frame_idx)

    def get_mp_norm_point(self, frame_idx, pt_name):
        return self.mp_result.get_norm_point(frame_idx, pt_name)

    def get_mp_norm_point_path(self, pt_name):
        """Return a list of (x, y) norm coord of the point in entire video"""
        return [
            self.mp_result.get_mp_norm_point(idx, pt_name) 
                    for idx in range(self.num_frames)
        ]


    # ML model for pose detection.
    def get_golf_pose(self, frame_idx):
        """ Return the golf pose enum type for the frame.
            If no pose detected then return state Unknown.
        """
        return self.pose_result.poses[frame_idx]

    # Club head screen point
    def get_club_head_point(self, frame_idx):
        return self.club_head_result.points[frame_idx]
    
    #
    # Visualize golf swing.
    # 
    def draw_frame(self, frame_idx, background_frame):
        # Draw media pipe
        self.mp_result.draw_frame(frame_idx, background_frame)

        (h, w, _) = background_frame.shape
        # Draw a line from the hand to the club head.
        club_head_point = self.get_club_head_point(frame_idx)
        if club_head_point:
            (x1, y1) = club_head_point
            right_thumb = self.get_mp_norm_point(frame_idx, "right_thumb")
            (x2, y2) = image_utils.scale_norm_point(right_thumb, w, h)
            cv2.line(background_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    