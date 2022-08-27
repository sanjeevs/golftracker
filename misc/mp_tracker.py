
""" Auto Generated tracker from script misc/gen_mp_tracker.py.DO NOT HAND EDIT !!"""

from collections import namedtuple
import mediapipe as mp
mp_pose = mp.solutions.pose



Nose = namedtuple("Nose", "x y")


def add_nose(trackers, x, y):
    """Add nose tracker to the list with normalized coordinates."""
    nose = Nose(x, y)
    if "nose" in trackers.keys():
        raise ValueError("Duplicate value of nose tracker")
    trackers["nose"] = nose
    
    


LeftEyeInner = namedtuple("LeftEyeInner", "x y")


def add_left_eye_inner(trackers, x, y):
    """Add left_eye_inner tracker to the list with normalized coordinates."""
    left_eye_inner = LeftEyeInner(x, y)
    if "left_eye_inner" in trackers.keys():
        raise ValueError("Duplicate value of left_eye_inner tracker")
    trackers["left_eye_inner"] = left_eye_inner
    
    


LeftEye = namedtuple("LeftEye", "x y")


def add_left_eye(trackers, x, y):
    """Add left_eye tracker to the list with normalized coordinates."""
    left_eye = LeftEye(x, y)
    if "left_eye" in trackers.keys():
        raise ValueError("Duplicate value of left_eye tracker")
    trackers["left_eye"] = left_eye
    
    


LeftEyeOuter = namedtuple("LeftEyeOuter", "x y")


def add_left_eye_outer(trackers, x, y):
    """Add left_eye_outer tracker to the list with normalized coordinates."""
    left_eye_outer = LeftEyeOuter(x, y)
    if "left_eye_outer" in trackers.keys():
        raise ValueError("Duplicate value of left_eye_outer tracker")
    trackers["left_eye_outer"] = left_eye_outer
    
    


RightEyeInner = namedtuple("RightEyeInner", "x y")


def add_right_eye_inner(trackers, x, y):
    """Add right_eye_inner tracker to the list with normalized coordinates."""
    right_eye_inner = RightEyeInner(x, y)
    if "right_eye_inner" in trackers.keys():
        raise ValueError("Duplicate value of right_eye_inner tracker")
    trackers["right_eye_inner"] = right_eye_inner
    
    


RightEye = namedtuple("RightEye", "x y")


def add_right_eye(trackers, x, y):
    """Add right_eye tracker to the list with normalized coordinates."""
    right_eye = RightEye(x, y)
    if "right_eye" in trackers.keys():
        raise ValueError("Duplicate value of right_eye tracker")
    trackers["right_eye"] = right_eye
    
    


RightEyeOuter = namedtuple("RightEyeOuter", "x y")


def add_right_eye_outer(trackers, x, y):
    """Add right_eye_outer tracker to the list with normalized coordinates."""
    right_eye_outer = RightEyeOuter(x, y)
    if "right_eye_outer" in trackers.keys():
        raise ValueError("Duplicate value of right_eye_outer tracker")
    trackers["right_eye_outer"] = right_eye_outer
    
    


LeftEar = namedtuple("LeftEar", "x y")


def add_left_ear(trackers, x, y):
    """Add left_ear tracker to the list with normalized coordinates."""
    left_ear = LeftEar(x, y)
    if "left_ear" in trackers.keys():
        raise ValueError("Duplicate value of left_ear tracker")
    trackers["left_ear"] = left_ear
    
    


RightEar = namedtuple("RightEar", "x y")


def add_right_ear(trackers, x, y):
    """Add right_ear tracker to the list with normalized coordinates."""
    right_ear = RightEar(x, y)
    if "right_ear" in trackers.keys():
        raise ValueError("Duplicate value of right_ear tracker")
    trackers["right_ear"] = right_ear
    
    


MouthLeft = namedtuple("MouthLeft", "x y")


def add_mouth_left(trackers, x, y):
    """Add mouth_left tracker to the list with normalized coordinates."""
    mouth_left = MouthLeft(x, y)
    if "mouth_left" in trackers.keys():
        raise ValueError("Duplicate value of mouth_left tracker")
    trackers["mouth_left"] = mouth_left
    
    


MouthRight = namedtuple("MouthRight", "x y")


def add_mouth_right(trackers, x, y):
    """Add mouth_right tracker to the list with normalized coordinates."""
    mouth_right = MouthRight(x, y)
    if "mouth_right" in trackers.keys():
        raise ValueError("Duplicate value of mouth_right tracker")
    trackers["mouth_right"] = mouth_right
    
    


LeftShoulder = namedtuple("LeftShoulder", "x y")


def add_left_shoulder(trackers, x, y):
    """Add left_shoulder tracker to the list with normalized coordinates."""
    left_shoulder = LeftShoulder(x, y)
    if "left_shoulder" in trackers.keys():
        raise ValueError("Duplicate value of left_shoulder tracker")
    trackers["left_shoulder"] = left_shoulder
    
    


RightShoulder = namedtuple("RightShoulder", "x y")


def add_right_shoulder(trackers, x, y):
    """Add right_shoulder tracker to the list with normalized coordinates."""
    right_shoulder = RightShoulder(x, y)
    if "right_shoulder" in trackers.keys():
        raise ValueError("Duplicate value of right_shoulder tracker")
    trackers["right_shoulder"] = right_shoulder
    
    


LeftElbow = namedtuple("LeftElbow", "x y")


def add_left_elbow(trackers, x, y):
    """Add left_elbow tracker to the list with normalized coordinates."""
    left_elbow = LeftElbow(x, y)
    if "left_elbow" in trackers.keys():
        raise ValueError("Duplicate value of left_elbow tracker")
    trackers["left_elbow"] = left_elbow
    
    


RightElbow = namedtuple("RightElbow", "x y")


def add_right_elbow(trackers, x, y):
    """Add right_elbow tracker to the list with normalized coordinates."""
    right_elbow = RightElbow(x, y)
    if "right_elbow" in trackers.keys():
        raise ValueError("Duplicate value of right_elbow tracker")
    trackers["right_elbow"] = right_elbow
    
    


LeftWrist = namedtuple("LeftWrist", "x y")


def add_left_wrist(trackers, x, y):
    """Add left_wrist tracker to the list with normalized coordinates."""
    left_wrist = LeftWrist(x, y)
    if "left_wrist" in trackers.keys():
        raise ValueError("Duplicate value of left_wrist tracker")
    trackers["left_wrist"] = left_wrist
    
    


RightWrist = namedtuple("RightWrist", "x y")


def add_right_wrist(trackers, x, y):
    """Add right_wrist tracker to the list with normalized coordinates."""
    right_wrist = RightWrist(x, y)
    if "right_wrist" in trackers.keys():
        raise ValueError("Duplicate value of right_wrist tracker")
    trackers["right_wrist"] = right_wrist
    
    


LeftPinky = namedtuple("LeftPinky", "x y")


def add_left_pinky(trackers, x, y):
    """Add left_pinky tracker to the list with normalized coordinates."""
    left_pinky = LeftPinky(x, y)
    if "left_pinky" in trackers.keys():
        raise ValueError("Duplicate value of left_pinky tracker")
    trackers["left_pinky"] = left_pinky
    
    


RightPinky = namedtuple("RightPinky", "x y")


def add_right_pinky(trackers, x, y):
    """Add right_pinky tracker to the list with normalized coordinates."""
    right_pinky = RightPinky(x, y)
    if "right_pinky" in trackers.keys():
        raise ValueError("Duplicate value of right_pinky tracker")
    trackers["right_pinky"] = right_pinky
    
    


LeftIndex = namedtuple("LeftIndex", "x y")


def add_left_index(trackers, x, y):
    """Add left_index tracker to the list with normalized coordinates."""
    left_index = LeftIndex(x, y)
    if "left_index" in trackers.keys():
        raise ValueError("Duplicate value of left_index tracker")
    trackers["left_index"] = left_index
    
    


RightIndex = namedtuple("RightIndex", "x y")


def add_right_index(trackers, x, y):
    """Add right_index tracker to the list with normalized coordinates."""
    right_index = RightIndex(x, y)
    if "right_index" in trackers.keys():
        raise ValueError("Duplicate value of right_index tracker")
    trackers["right_index"] = right_index
    
    


LeftThumb = namedtuple("LeftThumb", "x y")


def add_left_thumb(trackers, x, y):
    """Add left_thumb tracker to the list with normalized coordinates."""
    left_thumb = LeftThumb(x, y)
    if "left_thumb" in trackers.keys():
        raise ValueError("Duplicate value of left_thumb tracker")
    trackers["left_thumb"] = left_thumb
    
    


RightThumb = namedtuple("RightThumb", "x y")


def add_right_thumb(trackers, x, y):
    """Add right_thumb tracker to the list with normalized coordinates."""
    right_thumb = RightThumb(x, y)
    if "right_thumb" in trackers.keys():
        raise ValueError("Duplicate value of right_thumb tracker")
    trackers["right_thumb"] = right_thumb
    
    


LeftHip = namedtuple("LeftHip", "x y")


def add_left_hip(trackers, x, y):
    """Add left_hip tracker to the list with normalized coordinates."""
    left_hip = LeftHip(x, y)
    if "left_hip" in trackers.keys():
        raise ValueError("Duplicate value of left_hip tracker")
    trackers["left_hip"] = left_hip
    
    


RightHip = namedtuple("RightHip", "x y")


def add_right_hip(trackers, x, y):
    """Add right_hip tracker to the list with normalized coordinates."""
    right_hip = RightHip(x, y)
    if "right_hip" in trackers.keys():
        raise ValueError("Duplicate value of right_hip tracker")
    trackers["right_hip"] = right_hip
    
    


LeftKnee = namedtuple("LeftKnee", "x y")


def add_left_knee(trackers, x, y):
    """Add left_knee tracker to the list with normalized coordinates."""
    left_knee = LeftKnee(x, y)
    if "left_knee" in trackers.keys():
        raise ValueError("Duplicate value of left_knee tracker")
    trackers["left_knee"] = left_knee
    
    


RightKnee = namedtuple("RightKnee", "x y")


def add_right_knee(trackers, x, y):
    """Add right_knee tracker to the list with normalized coordinates."""
    right_knee = RightKnee(x, y)
    if "right_knee" in trackers.keys():
        raise ValueError("Duplicate value of right_knee tracker")
    trackers["right_knee"] = right_knee
    
    


LeftAnkle = namedtuple("LeftAnkle", "x y")


def add_left_ankle(trackers, x, y):
    """Add left_ankle tracker to the list with normalized coordinates."""
    left_ankle = LeftAnkle(x, y)
    if "left_ankle" in trackers.keys():
        raise ValueError("Duplicate value of left_ankle tracker")
    trackers["left_ankle"] = left_ankle
    
    


RightAnkle = namedtuple("RightAnkle", "x y")


def add_right_ankle(trackers, x, y):
    """Add right_ankle tracker to the list with normalized coordinates."""
    right_ankle = RightAnkle(x, y)
    if "right_ankle" in trackers.keys():
        raise ValueError("Duplicate value of right_ankle tracker")
    trackers["right_ankle"] = right_ankle
    
    


LeftHeel = namedtuple("LeftHeel", "x y")


def add_left_heel(trackers, x, y):
    """Add left_heel tracker to the list with normalized coordinates."""
    left_heel = LeftHeel(x, y)
    if "left_heel" in trackers.keys():
        raise ValueError("Duplicate value of left_heel tracker")
    trackers["left_heel"] = left_heel
    
    


RightHeel = namedtuple("RightHeel", "x y")


def add_right_heel(trackers, x, y):
    """Add right_heel tracker to the list with normalized coordinates."""
    right_heel = RightHeel(x, y)
    if "right_heel" in trackers.keys():
        raise ValueError("Duplicate value of right_heel tracker")
    trackers["right_heel"] = right_heel
    
    


LeftFootIndex = namedtuple("LeftFootIndex", "x y")


def add_left_foot_index(trackers, x, y):
    """Add left_foot_index tracker to the list with normalized coordinates."""
    left_foot_index = LeftFootIndex(x, y)
    if "left_foot_index" in trackers.keys():
        raise ValueError("Duplicate value of left_foot_index tracker")
    trackers["left_foot_index"] = left_foot_index
    
    


RightFootIndex = namedtuple("RightFootIndex", "x y")


def add_right_foot_index(trackers, x, y):
    """Add right_foot_index tracker to the list with normalized coordinates."""
    right_foot_index = RightFootIndex(x, y)
    if "right_foot_index" in trackers.keys():
        raise ValueError("Duplicate value of right_foot_index tracker")
    trackers["right_foot_index"] = right_foot_index
    
    


def add_mp_landmarks(trackers, landmark):
    """Add media pipe landmarks to tracker list. """


    add_nose(trackers, landmark[mp_pose.PoseLandmark.NOSE].x,
                   landmark[mp_pose.PoseLandmark.NOSE].y)


    add_left_eye_inner(trackers, landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].x,
                   landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].y)


    add_left_eye(trackers, landmark[mp_pose.PoseLandmark.LEFT_EYE].x,
                   landmark[mp_pose.PoseLandmark.LEFT_EYE].y)


    add_left_eye_outer(trackers, landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].x,
                   landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].y)


    add_right_eye_inner(trackers, landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].y)


    add_right_eye(trackers, landmark[mp_pose.PoseLandmark.RIGHT_EYE].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_EYE].y)


    add_right_eye_outer(trackers, landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_EYE_OUTER].y)


    add_left_ear(trackers, landmark[mp_pose.PoseLandmark.LEFT_EAR].x,
                   landmark[mp_pose.PoseLandmark.LEFT_EAR].y)


    add_right_ear(trackers, landmark[mp_pose.PoseLandmark.RIGHT_EAR].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_EAR].y)


    add_mouth_left(trackers, landmark[mp_pose.PoseLandmark.MOUTH_LEFT].x,
                   landmark[mp_pose.PoseLandmark.MOUTH_LEFT].y)


    add_mouth_right(trackers, landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].x,
                   landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].y)


    add_left_shoulder(trackers, landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                   landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y)


    add_right_shoulder(trackers, landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y)


    add_left_elbow(trackers, landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                   landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y)


    add_right_elbow(trackers, landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y)


    add_left_wrist(trackers, landmark[mp_pose.PoseLandmark.LEFT_WRIST].x,
                   landmark[mp_pose.PoseLandmark.LEFT_WRIST].y)


    add_right_wrist(trackers, landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y)


    add_left_pinky(trackers, landmark[mp_pose.PoseLandmark.LEFT_PINKY].x,
                   landmark[mp_pose.PoseLandmark.LEFT_PINKY].y)


    add_right_pinky(trackers, landmark[mp_pose.PoseLandmark.RIGHT_PINKY].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_PINKY].y)


    add_left_index(trackers, landmark[mp_pose.PoseLandmark.LEFT_INDEX].x,
                   landmark[mp_pose.PoseLandmark.LEFT_INDEX].y)


    add_right_index(trackers, landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y)


    add_left_thumb(trackers, landmark[mp_pose.PoseLandmark.LEFT_THUMB].x,
                   landmark[mp_pose.PoseLandmark.LEFT_THUMB].y)


    add_right_thumb(trackers, landmark[mp_pose.PoseLandmark.RIGHT_THUMB].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_THUMB].y)


    add_left_hip(trackers, landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                   landmark[mp_pose.PoseLandmark.LEFT_HIP].y)


    add_right_hip(trackers, landmark[mp_pose.PoseLandmark.RIGHT_HIP].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_HIP].y)


    add_left_knee(trackers, landmark[mp_pose.PoseLandmark.LEFT_KNEE].x,
                   landmark[mp_pose.PoseLandmark.LEFT_KNEE].y)


    add_right_knee(trackers, landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y)


    add_left_ankle(trackers, landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                   landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y)


    add_right_ankle(trackers, landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y)


    add_left_heel(trackers, landmark[mp_pose.PoseLandmark.LEFT_HEEL].x,
                   landmark[mp_pose.PoseLandmark.LEFT_HEEL].y)


    add_right_heel(trackers, landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y)


    add_left_foot_index(trackers, landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x,
                   landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y)


    add_right_foot_index(trackers, landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x,
                   landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y)

