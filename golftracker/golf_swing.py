#
# Root object
# Data storage as processing of the video continues.

import json
import copy
import gt_const
from pose_data import PoseData


class GolfSwing:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.mp_pose_frame_landmarks = []  # Media pipe pose output

    def get_pose_data(self, idx):
        """ Return the pose data at the frame specifiec. """
        p = PoseData(self.mp_pose_frame_landmarks[idx], self.height, self.width)
        return p

    def pose_row(self, idx):
        return self.mp_pose_frame_landmarks[idx]

    def pose_row_header(self):
        """ Return the header row for pose data."""

        header = []
        for entry in gt_const.MP_POSE_LANDMARKS:
            for i in ["_x", "_y", "_z", "_v"]:
                header.append(entry + i)
        return header

    def _out_format(self):
        """ Generate output format for json serialization. """

        fmt = {}
        fmt['height'] = self.height
        fmt['width'] = self.width

        # Per Frame landmark information.
        frames_lst = []
        for idx in range(len(self.mp_pose_frame_landmarks)):
            entry = {}
            entry["frame_idx"] = idx
            entry["mp_pose_landmarks"] = []
            for item in self.mp_pose_frame_landmarks[idx]:
                entry["mp_pose_landmarks"] += [item.x, item.y, item.z, item.visibility]
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
