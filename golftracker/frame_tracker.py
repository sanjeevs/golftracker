
""" 
    Auto Generated tracker from script misc/gen_frame_tracker.py.
    DO NOT HAND EDIT !!

"""
import json

import mediapipe as mp
mp_pose = mp.solutions.pose

class FrameTracker:
    def __init__(self):
        self.trackers = {}

        # Initialize all the trackers with default 0, 0 coord

        self.trackers["nose"] = [0, 0]
        self.trackers["left_eye_inner"] = [0, 0]
        self.trackers["left_eye"] = [0, 0]
        self.trackers["left_eye_outer"] = [0, 0]
        self.trackers["right_eye_inner"] = [0, 0]
        self.trackers["right_eye"] = [0, 0]
        self.trackers["right_eye_outer"] = [0, 0]
        self.trackers["left_ear"] = [0, 0]
        self.trackers["right_ear"] = [0, 0]
        self.trackers["mouth_left"] = [0, 0]
        self.trackers["mouth_right"] = [0, 0]
        self.trackers["left_shoulder"] = [0, 0]
        self.trackers["right_shoulder"] = [0, 0]
        self.trackers["left_elbow"] = [0, 0]
        self.trackers["right_elbow"] = [0, 0]
        self.trackers["left_wrist"] = [0, 0]
        self.trackers["right_wrist"] = [0, 0]
        self.trackers["left_pinky"] = [0, 0]
        self.trackers["right_pinky"] = [0, 0]
        self.trackers["left_index"] = [0, 0]
        self.trackers["right_index"] = [0, 0]
        self.trackers["left_thumb"] = [0, 0]
        self.trackers["right_thumb"] = [0, 0]
        self.trackers["left_hip"] = [0, 0]
        self.trackers["right_hip"] = [0, 0]
        self.trackers["left_knee"] = [0, 0]
        self.trackers["right_knee"] = [0, 0]
        self.trackers["left_ankle"] = [0, 0]
        self.trackers["right_ankle"] = [0, 0]
        self.trackers["left_heel"] = [0, 0]
        self.trackers["right_heel"] = [0, 0]
        self.trackers["left_foot_index"] = [0, 0]
        self.trackers["right_foot_index"] = [0, 0]
        self.trackers["club_grip"] = [0, 0]
        self.trackers["club_heel"] = [0, 0]
        self.trackers["club_toe"] = [0, 0]

    def __setitem__(self, key, val):
        if key not in self.trackers:
            raise KeyError(f"Key '{key}' not a valid name")
        self.trackers[key] = val

    def __getitem__(self, key):
        if key not in self.trackers:
            return (0, 0)
        return self.trackers[key]

    def __len__(self):
        return len(self.trackers)

    def keys(self):
        return self.trackers.keys()

    def to_json_str(self):
        return json.dumps(self.trackers)

    def to_json(self, fname):
        with open(fname, "w") as fh:
            json.dump(self.trackers, fh)

    def fm_json_str(self, str):
        self.trackers = json.loads(str)

    def fm_json(self, fname):
        with open(fname, "r") as fh:
            self.trackers = json.load(fh)

    def set_mp_trackers(self, landmark):
        """Add media pipe landmarks to tracker list. """ 

        self.trackers["nose"] = [landmark[mp_pose.PoseLandmark.NOSE].x,
                                landmark[mp_pose.PoseLandmark.NOSE].y]

        self.trackers["left_eye_inner"] = [landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].y]

        self.trackers["left_eye"] = [landmark[mp_pose.PoseLandmark.LEFT_EYE].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EYE].y]

        self.trackers["left_eye_outer"] = [landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].y]

        self.trackers["right_eye_inner"] = [landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].y]

        self.trackers["right_eye"] = [landmark[mp_pose.PoseLandmark.RIGHT_EYE].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EYE].y]

        self.trackers["right_eye_outer"] = [landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER].y]

        self.trackers["left_ear"] = [landmark[mp_pose.PoseLandmark.LEFT_EAR].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EAR].y]

        self.trackers["right_ear"] = [landmark[mp_pose.PoseLandmark.RIGHT_EAR].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EAR].y]

        self.trackers["mouth_left"] = [landmark[mp_pose.PoseLandmark.MOUTH_LEFT].x,
                                landmark[mp_pose.PoseLandmark.MOUTH_LEFT].y]

        self.trackers["mouth_right"] = [landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].x,
                                landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].y]

        self.trackers["left_shoulder"] = [landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                                landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y]

        self.trackers["right_shoulder"] = [landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y]

        self.trackers["left_elbow"] = [landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                                landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y]

        self.trackers["right_elbow"] = [landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y]

        self.trackers["left_wrist"] = [landmark[mp_pose.PoseLandmark.LEFT_WRIST].x,
                                landmark[mp_pose.PoseLandmark.LEFT_WRIST].y]

        self.trackers["right_wrist"] = [landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y]

        self.trackers["left_pinky"] = [landmark[mp_pose.PoseLandmark.LEFT_PINKY].x,
                                landmark[mp_pose.PoseLandmark.LEFT_PINKY].y]

        self.trackers["right_pinky"] = [landmark[mp_pose.PoseLandmark.RIGHT_PINKY].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_PINKY].y]

        self.trackers["left_index"] = [landmark[mp_pose.PoseLandmark.LEFT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.LEFT_INDEX].y]

        self.trackers["right_index"] = [landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y]

        self.trackers["left_thumb"] = [landmark[mp_pose.PoseLandmark.LEFT_THUMB].x,
                                landmark[mp_pose.PoseLandmark.LEFT_THUMB].y]

        self.trackers["right_thumb"] = [landmark[mp_pose.PoseLandmark.RIGHT_THUMB].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_THUMB].y]

        self.trackers["left_hip"] = [landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                                landmark[mp_pose.PoseLandmark.LEFT_HIP].y]

        self.trackers["right_hip"] = [landmark[mp_pose.PoseLandmark.RIGHT_HIP].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_HIP].y]

        self.trackers["left_knee"] = [landmark[mp_pose.PoseLandmark.LEFT_KNEE].x,
                                landmark[mp_pose.PoseLandmark.LEFT_KNEE].y]

        self.trackers["right_knee"] = [landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]

        self.trackers["left_ankle"] = [landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                                landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y]

        self.trackers["right_ankle"] = [landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y]

        self.trackers["left_heel"] = [landmark[mp_pose.PoseLandmark.LEFT_HEEL].x,
                                landmark[mp_pose.PoseLandmark.LEFT_HEEL].y]

        self.trackers["right_heel"] = [landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y]

        self.trackers["left_foot_index"] = [landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y]

        self.trackers["right_foot_index"] = [landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y]
