import json
import numpy as np
from golftracker import gt_const as gt


class GolfData:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.mp_frame_landmarks = [[]] * num_frames
        self.golf_poses = {}

    # 
    # Query inteface
    #
    def get_mp_landmarks(self, frame_idx):
        return self.mp_frame_landmarks[frame_idx]

    def get_mp_landmarks_flat_row(self, frame_idx):
        """ Return media pipe landmarks as a list of tuple (x, y, z, v) normalized coordinates """
        rslt = self.get_mp_landmarks(frame_idx)
        row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in rslt.landmark]).flatten())
        return row

    def get_golf_pose(self, frame_idx):
        if frame_idx in self.golf_poses.keys():
            return self.golf_poses[frame_idx][0]
        else:
            return gt.GolfPose.Unknown

    def get_golf_pose_prob(self, frame_idx):
        if frame_idx in self.golf_poses.keys():
            return self.golf_poses[frame_idx][1]
        else:
            return 0.0

    def get_pose_frames(self, golf_pose):
        lst = []
        for frame_idx in self.golf_poses.keys():
            if self.get_golf_pose(frame_idx) == golf_pose:
                lst.append(frame_idx)
        return lst

    # 
    # Command Interface
    # 
    def set_mp_landmarks(self, frame_idx, landmarks):
        self.mp_frame_landmarks[frame_idx] = landmarks

    def set_golf_pose(self, frame_idx, golf_pose, prob):
        self.golf_poses[frame_idx] = (golf_pose, prob)

    
   