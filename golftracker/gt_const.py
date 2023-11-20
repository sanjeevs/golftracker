from enum import Enum
from mediapipe.framework.formats import landmark_pb2
import numpy as np

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

ML_POSE_PROB_THRESHOLD = 0.7

class GolfPose(Enum):
    RhStart = 1
    RhTop = 2
    RhFinish = 3
    LhStart = 4
    LhTop = 5
    LhFinish = 6
    Unknown = 100

def abbrev_pose(pose):
    mapping = {
        GolfPose.RhStart: 'S',
        GolfPose.RhTop: 'T',
        GolfPose.RhFinish: 'F',
        GolfPose.Unknown: 'U',
        GolfPose.LhStart: 's',
        GolfPose.LhTop: 't',
        GolfPose.LhFinish: 'f',
    }
    return mapping[pose]

def print_golf_poses(poses):
    for i in range(0, len(poses), 16):
        print(''.join(abbrev(pose) for pose in poses[i:i+16]))

class Handedness(Enum):
    LeftHanded=1
    RightHanded=2
    Unknown=3

def mp_landmark_row_header():
    """ Return the header row for pose data."""

    header = []
    for entry in MP_POSE_LANDMARKS:
        for i in ["_x", "_y", "_z", "_v"]:
            header.append(entry + i)

    return header

def num_mp_landmarks():
    return len(MP_POSE_LANDMARKS)


def create_pb_normalized_landmarks(lst):
    """ Given a list of 4 member entries [x0, y0, z0, v0, x1, y1, .., x31, y31, z31, v31] return landmarks. """
    x = 0
    landmark_lst = []
    while x < len(lst):
        n = landmark_pb2.NormalizedLandmark(x=lst[x], y=lst[x+1], z=lst[x+2], visibility=lst[x+3])
        landmark_lst.append(n)
        x += 4

    reconstructed = landmark_pb2.NormalizedLandmarkList(landmark=landmark_lst)
    return reconstructed

def get_mp_landmarks_flat_row(frame_landmark):
    """ 
    Helper function to convert media pipe landmark list into a flat row.

    :param frame_landmarks: List of proto buf for each landmark in a list.
    :return: list of tuple (x, y, z, v) normalized coordinates
    :rtype: list    
    """
    if frame_landmark:
        return list(
            np.array(
                [
                [landmark.x, landmark.y, landmark.z, landmark.visibility]
                for landmark in frame_landmark.landmark
                ]
                ).flatten()
            )
    else:
        return []