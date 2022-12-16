from enum import Enum


MP_POSE_LANDMARKS = [
    "nose",
    "left_eye_inner",
    "left_eye",
    "left_eye_outer",
    "right_eye_inner",
    "right_eye",
    "right_eye_outer",
    "left_ear",
    "right_ear",
    "mouth_left",
    "mouth_right",
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_wrist",
    "right_wrist",
    "left_pinky",
    "right_pinky",
    "left_index",
    "right_index",
    "left_thumb",
    "right_thumb",
    "left_hip",
    "right_hip",
    "left_knee",
    "right_knee",
    "left_ankle",
    "right_ankle",
    "left_heel",
    "right_heel",
    "left_foot_index",
    "right_foot_index",
]


class GolfPose(Enum):
    RhStart = 1
    RhTop = 2
    RhFinish = 3
    LhStart = 4
    LhTop = 5
    LhFinish = 6


def pose_row_header():
    """ Return the header row for pose data."""

    header = []
    for entry in MP_POSE_LANDMARKS:
        for i in ["_x", "_y", "_z", "_v"]:
            header.append(entry + i)

    return header
