#
# Root object
# Data storage as processing of the video continues.
#
# Root class
#
import pandas as pd
import numpy as np
import pickle
from collections import defaultdict
import os

from golftracker import golf_data
from golftracker import gt_const
from golftracker import points
from golftracker import video_utils
from golftracker import file_utils

import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

class GolfSwing:
    def __init__(self, height, width, num_frames, fps=30):
        self.height = height
        self.width = width
        self.num_frames = num_frames
        self.fps = fps
        self.video_fname = ""
        self.data = golf_data.GolfData(num_frames)

    def set_meta_info(self, video_fname):
        self.video_fname = file_utils.basename(video_fname)
        self.video_size = os.path.getsize(video_fname)
    
    # Query Interface
    # Return all the list.

    def get_video_frames(self):
        """Return the video frames from video fname. """
        (frames, _) = video_utils.split_video_to_frames(self.video_fname)
        return frames

    def get_screen_points(self, frame_idx):
        """Return the x, y coordinates of all points on the frame. """
        row = self.get_mp_landmarks_flat_row(frame_idx)
        p = points.Points(
            row, self.height, self.width
        )
        return p

    def get_golf_pose(self, frame_idx):
        """ Return the golf pose enum type for the frame.
            If no pose detected then return state Unknown.
        """
        return self.data.get_golf_pose(frame_idx)

    def get_pose_frames(self, golf_pose):
        """Return all the frames that match the given pose."""
        return self.data.get_pose_frames(golf_pose)

    def get_mp_landmarks_flat_row(self, frame_idx):
        """Helper function to return media pipe values in a flat row. 
           used for training data for ml pose model.
        """
        return self.data.get_mp_landmarks_flat_row(frame_idx)

    def to_frames(self, incoming_frames=[]):
        frames = []

        for frame_idx in range(self.num_frames):
            if frame_idx < len(incoming_frames):
                frame = incoming_frames[frame_idx]
            else:
                frame = np.zeros([self.height, self.width, 3], dtype=np.uint8)
            #reconstructed = self.data.get_pb_normalized_landmarks(frame_idx)
            reconstructed = self.data.get_mp_landmarks(frame_idx)
        
            mp_drawing.draw_landmarks(frame, reconstructed, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

            frames.append(frame)

        return frames

    def get_poses_in_frames(self):
        rslt = defaultdict(list)
        for frame_idx in range(self.num_frames):
            pose = self.get_golf_pose(frame_idx)
            if pose:
                rslt[pose].append(frame_idx)
        return rslt

    #
    # Command interface
    # Change the state of the object.

    def set_golf_pose(self, frame_idx, golf_pose, prob):
        self.data.set_golf_pose(frame_idx, golf_pose, prob)

    def set_mp_landmarks(self, frame_idx, landmarks):
        self.data.set_mp_landmarks(frame_idx, landmarks)

    

    