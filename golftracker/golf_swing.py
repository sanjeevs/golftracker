#
# Root object
# Data storage as processing of the video continues.

import json
import copy
from golftracker import golf_data
from golftracker import gt_const
from golftracker import points
import pandas as pd
import numpy as np
import pickle

import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils

class GolfSwing:
    def __init__(self, height, width, num_frames):
        self.height = height
        self.width = width
        self.num_frames = num_frames
        self.data = golf_data.GolfData(num_frames)

    def get_screen_points(self, frame_idx):
        """ Return the points on the frame. """
        p = points.Points(
            self.data.get_mp_landmarks(frame_idx), self.height, self.width
        )
        return p

    def mp_landmarks_flat_row(self, frame_idx):
        return self.data.mp_landmarks_flat_row(frame_idx)

    def set_golf_pose(self, frame_idx, golf_pose, prob):
        self.data.set_golf_pose(frame_idx, golf_pose, prob)

    def get_golf_pose(self, frame_idx):
        entry = self.data.get_golf_pose(frame_idx)
        return entry

    def set_mp_landmarks(self, frame_idx, landmarks):
        self.data.set_mp_landmarks(frame_idx, landmarks)

    def to_frames(self):
        frames = []

        for frame_idx in range(self.num_frames()):
            frame = np.zeros([self.height, self.width, 3], dtype=np.uint8)
            reconstructed = self.data.get_pb_normalized_landmarks(frame_idx)
        
            mp_drawing.draw_landmarks(frame, reconstructed, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

            frames.append(frame)

        return frames