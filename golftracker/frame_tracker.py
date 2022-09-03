
""" 
    Auto Generated tracker from script misc/gen_frame_tracker.py.
    DO NOT HAND EDIT !!

"""
import mediapipe as mp
mp_pose = mp.solutions.pose

class FrameTracker:
    def __init__(self):
        self.trackers = {}
        self.names = []

        # Initialize all the trackers with default 0, 0 coord

        self.names.append("nose")
        self.names.append("left_eye_inner")
        self.names.append("left_eye")
        self.names.append("left_eye_outer")
        self.names.append("right_eye_inner")
        self.names.append("right_eye")
        self.names.append("right_eye_outer")
        self.names.append("left_ear")
        self.names.append("right_ear")
        self.names.append("mouth_left")
        self.names.append("mouth_right")
        self.names.append("left_shoulder")
        self.names.append("right_shoulder")
        self.names.append("left_elbow")
        self.names.append("right_elbow")
        self.names.append("left_wrist")
        self.names.append("right_wrist")
        self.names.append("left_pinky")
        self.names.append("right_pinky")
        self.names.append("left_index")
        self.names.append("right_index")
        self.names.append("left_thumb")
        self.names.append("right_thumb")
        self.names.append("left_hip")
        self.names.append("right_hip")
        self.names.append("left_knee")
        self.names.append("right_knee")
        self.names.append("left_ankle")
        self.names.append("right_ankle")
        self.names.append("left_heel")
        self.names.append("right_heel")
        self.names.append("left_foot_index")
        self.names.append("right_foot_index")
        self.names.append("club_grip")
        self.names.append("club_heel")
        self.names.append("club_toe")

    def __setitem__(self, key, val):
        if key not in self.names:
            raise KeyError(f"Key '{key}' not a valid name")
        self.trackers[key] = val

    def __getitem__(self, key):
        if key not in self.names:
            raise KeyError(f"Key '{key}' not a valid name")
        if key not in self.trackers:
            return (0, 0)
        return self.trackers[key]

    def __len__(self):
        return len(self.names)

    def keys(self):
        return self.names

    def set_mp_trackers(self, landmark):
        """Add media pipe landmarks to tracker list. """ 

        self.trackers["nose"] = (landmark[mp_pose.PoseLandmark.NOSE].x,
                                landmark[mp_pose.PoseLandmark.NOSE].y)

        self.trackers["left_eye_inner"] = (landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].y)

        self.trackers["left_eye"] = (landmark[mp_pose.PoseLandmark.LEFT_EYE].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EYE].y)

        self.trackers["left_eye_outer"] = (landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].y)

        self.trackers["right_eye_inner"] = (landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].y)

        self.trackers["right_eye"] = (landmark[mp_pose.PoseLandmark.RIGHT_EYE].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EYE].y)

        self.trackers["right_eye_outer"] = (landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER].y)

        self.trackers["left_ear"] = (landmark[mp_pose.PoseLandmark.LEFT_EAR].x,
                                landmark[mp_pose.PoseLandmark.LEFT_EAR].y)

        self.trackers["right_ear"] = (landmark[mp_pose.PoseLandmark.RIGHT_EAR].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_EAR].y)

        self.trackers["mouth_left"] = (landmark[mp_pose.PoseLandmark.MOUTH_LEFT].x,
                                landmark[mp_pose.PoseLandmark.MOUTH_LEFT].y)

        self.trackers["mouth_right"] = (landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].x,
                                landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].y)

        self.trackers["left_shoulder"] = (landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                                landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y)

        self.trackers["right_shoulder"] = (landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y)

        self.trackers["left_elbow"] = (landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                                landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y)

        self.trackers["right_elbow"] = (landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y)

        self.trackers["left_wrist"] = (landmark[mp_pose.PoseLandmark.LEFT_WRIST].x,
                                landmark[mp_pose.PoseLandmark.LEFT_WRIST].y)

        self.trackers["right_wrist"] = (landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y)

        self.trackers["left_pinky"] = (landmark[mp_pose.PoseLandmark.LEFT_PINKY].x,
                                landmark[mp_pose.PoseLandmark.LEFT_PINKY].y)

        self.trackers["right_pinky"] = (landmark[mp_pose.PoseLandmark.RIGHT_PINKY].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_PINKY].y)

        self.trackers["left_index"] = (landmark[mp_pose.PoseLandmark.LEFT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.LEFT_INDEX].y)

        self.trackers["right_index"] = (landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y)

        self.trackers["left_thumb"] = (landmark[mp_pose.PoseLandmark.LEFT_THUMB].x,
                                landmark[mp_pose.PoseLandmark.LEFT_THUMB].y)

        self.trackers["right_thumb"] = (landmark[mp_pose.PoseLandmark.RIGHT_THUMB].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_THUMB].y)

        self.trackers["left_hip"] = (landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                                landmark[mp_pose.PoseLandmark.LEFT_HIP].y)

        self.trackers["right_hip"] = (landmark[mp_pose.PoseLandmark.RIGHT_HIP].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_HIP].y)

        self.trackers["left_knee"] = (landmark[mp_pose.PoseLandmark.LEFT_KNEE].x,
                                landmark[mp_pose.PoseLandmark.LEFT_KNEE].y)

        self.trackers["right_knee"] = (landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y)

        self.trackers["left_ankle"] = (landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                                landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y)

        self.trackers["right_ankle"] = (landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y)

        self.trackers["left_heel"] = (landmark[mp_pose.PoseLandmark.LEFT_HEEL].x,
                                landmark[mp_pose.PoseLandmark.LEFT_HEEL].y)

        self.trackers["right_heel"] = (landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y)

        self.trackers["left_foot_index"] = (landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y)

        self.trackers["right_foot_index"] = (landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x,
                                landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y)
