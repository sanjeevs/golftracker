import json
import numpy as np
from golftracker import gt_const as gt

from mediapipe.framework.formats import landmark_pb2


class GolfData:
    def __init__(self, num_frames):
        self.mp_frame_landmarks = [[]] * num_frames
        self.golf_poses = []

    def set_mp_landmarks(self, frame_idx, landmarks):
        self.mp_frame_landmarks[frame_idx] = landmarks

    def get_mp_landmarks(self, frame_idx):
        return self.mp_frame_landmarks[frame_idx]

    def mp_landmarks_flat_row(self, frame_idx):
        """ Return media pipe landmarks as a single flat row of numbers. """
        landmarks = self.mp_frame_landmarks[frame_idx]
        row = list(
            np.array(
                [
                    [landmark.x, landmark.y, landmark.z, landmark.visibility]
                    for landmark in landmarks
                ]
            ).flatten()
        )
        return row

    def get_pb_normalized_landmarks(self, frame_idx):
        lst = self.mp_frame_landmarks[frame_idx]
        
        x = 0
        landmark_lst = []
        while x < len(lst):
            n = landmark_pb2.NormalizedLandmark(x=lst[x], y=lst[x+1], z=lst[x+2], visibility=lst[x+3])
            landmark_lst.append(n)
            x += 4

        reconstructed = landmark_pb2.NormalizedLandmarkList(landmark=landmark_lst)
        return reconstructed


    def set_golf_pose(self, frame_idx, golf_pose, prob):
        self.golf_poses.append((frame_idx, golf_pose, prob))

    def get_golf_pose(self, frame_idx):
        for entry in self.golf_poses:
            if entry[0] == frame_idx:
                return (gt.GolfPose(entry[1]), entry[2])
        return (None, 0.0)

    def to_dict(self):
        fmt = {}
        fmt["mp_frame_landmarks"] = self.mp_frame_landmarks
        fmt['golf_poses'] = []
        for frame_idx, pose, prob in self.golf_poses:
            fmt["golf_poses"].append([frame_idx, pose.name, prob])
        return fmt


def create_fm_dict(data):
    print(type(data))
    new_gd = GolfData(len(data["mp_frame_landmarks"]))
    new_gd.mp_frame_landmarks = data["mp_frame_landmarks"]
    for entry in data['golf_poses']:
        new_gd.golf_poses.append([entry[0], gt.GolfPose[entry[1]], entry[2]])
    return new_gd
