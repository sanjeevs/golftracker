''' Root class '''

from golftracker import media_pipe_landmarks
from golftracker import pose_result
from golftracker import club_head_result
from golftracker import video_utils
from golftracker import image_utils
from golftracker import gt_const as gt
import cv2
import json

class GolfSwing:
    def __init__(self, video_spec, video_input):
        self.video_spec = video_spec
        self.video_input = video_input

        # Lazy eval for frames.
        self.frames = []

        # Results
        self.num_frames = video_spec.num_frames
        self.mp_result = media_pipe_landmarks.MediaPipeLandmarks(self.num_frames)
        self.pose_result = pose_result.PoseResult(self.num_frames)
        self.club_head_result = club_head_result.ClubHeadResult(self.num_frames)

    # Get frames from video lazily
    def get_video_frames(self, scale=100):
        if not self.frames:
            (self.frames, _) = video_utils.split_video_to_frames(
                    self.video_input.fname, scale=scale,
                    rotate=0)
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
            self.mp_result.get_norm_point(idx, pt_name) 
                    for idx in range(self.video_spec.num_frames)
        ]


    # ML model for pose detection.
    def set_golf_pose(self, frame_idx, pose):
        self.pose_result.poses[frame_idx] = pose
        
    def get_golf_pose(self, frame_idx):
        """ Return the golf pose enum type for the frame.
            If no pose detected then return state Unknown.
        """
        return self.pose_result.poses[frame_idx]

    def get_golf_pose_sequence(self):
        start_idx = self.pose_result.get_first_start_pose_frame_idx()
        end_idx = self.pose_result.get_last_finish_pose_frame_idx()
        return (start_idx, end_idx)

    def get_norm_club_head_point(self, frame_idx):
        ''' Return the club head point. '''
        return self.club_head_result.norm_points[frame_idx]

    def get_norm_club_head_info(self, frame_idx):
        ''' Return the club head point and the source of calc. '''
        return (self.club_head_result.norm_points[frame_idx], 
                self.club_head_result.algos[frame_idx])
    
    # Club head result
    def init_club_head_result(self):
        self.club_head_result = club_head_result.ClubHeadResult(self.num_frames)

    #
    # Visualize golf swing.
    # 
    def draw_frame(self, frame_idx, background_frame, line_color='blue'):
        # Draw media pipe
        self.mp_result.draw_frame(frame_idx, background_frame, line_color)

        (h, w, _) = background_frame.shape
        # Draw a line from the hand to the club head.
        norm_club_head_pt, algo = self.get_norm_club_head_info(frame_idx)
        
        if norm_club_head_pt:
            x1, y1= image_utils.scale_norm_point(norm_club_head_pt, width=w, height=h)
            right_thumb = self.get_mp_norm_point(frame_idx, "right_thumb")
            x2, y2 = image_utils.scale_norm_point(right_thumb, w, h)
            if algo == "Label":
                cv2.line(background_frame, (int(x1), int(y1)), (x2, y2), (0, 0, 255), 2)
            else:
                cv2.line(background_frame, (int(x1), int(y1)), (x2, y2), (0, 255, 255), 2)

    # Write out json state for analysis

    def to_json(self, json_fname, compact=True):
        data = {
            "video_spec": self.video_spec._asdict(),
            "video_input": self.video_input._asdict(),
            "num_frames": self.num_frames,
            "pose_result": self.pose_result.serialize(),
            "club_head_result": self.club_head_result.serialize(),
            "mp_result": self.mp_result.serialize(),
        }

        # Write to json
        with open(json_fname, "w") as file:
            if compact:
                json.dump(data, file)
            else:
                json.dump(data, file, indent=4)