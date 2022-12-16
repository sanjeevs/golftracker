import json
import numpy as np
from golftracker import gt_const as gt

from mediapipe.framework.formats import landmark_pb2


class GolfData:
    def __init__(self, num_frames):
        self.mp_frame_landmarks = [None] * num_frames
        self.ml_poses = []

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


    def set_ml_pose(self, frame_idx, golf_pose, prob):
        self.ml_poses.append((frame_idx, golf_pose, prob))

    def get_ml_pose(self, frame_idx):
        for entry in self.ml_poses:
            if entry[0] == frame_idx:
                return (gt.GolfPose(entry[1]), entry[2])
        return (None, 0.0)

    def to_json(self):
        fmt = {}
        fmt["mp_frame_landmarks"] = self.mp_frame_landmarks
        fmt["ml_poses"] = self.ml_poses
        return json.dumps(fmt)


def create_fm_json_str(json_str):
    data = json.loads(json_str)
    new_gd = GolfData(len(data["mp_frame_landmarks"]))
    new_gd.mp_frame_landmarks = data["mp_frame_landmarks"]
    new_gd.ml_poses = data["ml_poses"]
    return new_gd
