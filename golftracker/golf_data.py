import json
import numpy as np
from golftracker import gt_const as gt


class GolfData:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.mp_frame_landmarks = [[]] * num_frames
        self.golf_poses = {}

    def set_mp_landmarks(self, frame_idx, landmarks):
        self.mp_frame_landmarks[frame_idx] = landmarks

    def get_mp_landmarks(self, frame_idx):
        return self.mp_frame_landmarks[frame_idx]

    def get_mp_landmarks_flat_row(self, frame_idx):
        """ Return media pipe landmarks as a list of tuple (x, y, z, v) normalized coordinates """
        rslt = self.mp_frame_landmarks[frame_idx].landmark
        row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in rslt]).flatten())
        return row

    def set_golf_pose(self, frame_idx, golf_pose, prob):
        self.golf_poses[frame_idx] = (golf_pose, prob)

    def get_golf_pose(self, frame_idx):
        if frame_idx in self.golf_poses.keys():
            return self.golf_poses[frame_idx]
        else:
            return None