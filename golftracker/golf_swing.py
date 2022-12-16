#
# Root object
# Data storage as processing of the video continues.

import json
import copy
from golftracker import gt_const
from golftracker import pose_data
import pandas as pd 
import numpy as np


class GolfSwing:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.mp_frame_landmarks = []    # Media pipe pose output
        self.ml_frame_predictions = {}  # ML model predicted poses.


    def get_frame_points(self, frame_idx):
        """ Return the pose data at the frame specifics. """
        p = points.Points(self.mp_frame_landmarks[frame_idx], self.height, self.width)
        return p


    def num_frames(self):
        return len(self.mp_frame_landmarks)


    def pose_row(self, idx):
        pose = self.mp_frame_landmarks[idx]
        row = list(
                    np.array(
                        [
                            [landmark.x, landmark.y, landmark.z, landmark.visibility]
                            for landmark in pose
                        ]
                    ).flatten()
                )
        return row

   

    def analytics(self, model):
        num_mp_poses = len(self.mp_frame_landmarks)
        print(">>Running ML model on {num_mp_poses} frames of media pipe data")
        for idx in range(num_mp_poses):
            X = pd.DataFrame([self.pose_row(idx)])

            pose_class = model.predict(X)[0]
            pose_prob = model.predict_proba(X)[0]
            max_prob = round(pose_prob[np.argmax(pose_prob)], 2)

            if max_prob > 0.50:
                self.ml_frame_predictions[idx] = (pose_class, max_prob)

    def _out_format(self):
        """ Generate output format for json serialization. """

        fmt = {}
        fmt['height'] = self.height
        fmt['width'] = self.width

        # Per Frame landmark information.
        frames_lst = []
        for idx in range(len(self.mp_frame_landmarks)):
            entry = {}
            entry["frame_idx"] = idx
            entry["mp_pose_landmarks"] = []
            for item in self.mp_frame_landmarks[idx]:
                entry["mp_pose_landmarks"] += [item.x, item.y, item.z, item.visibility]
            
            if idx in self.ml_frame_predictions.keys():
                entry["pose_class"] = (self.ml_frame_predictions[idx][0], self.ml_frame_predictions[idx][1])

            frames_lst.append(entry)

        fmt['frames'] = frames_lst
        return fmt

    def __str__(self):
        return str(self._out_format())

    def __repr__(self):
        return json.dumps(self._out_format())

    def to_json(self):
        return self.__repr__()

    def save_to_json(self, fname):
        with open(fname, "w") as fh:
            json.dump(self._out_format(), fh)
