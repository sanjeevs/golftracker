
""" Auto Generated tracker from script gen_tracker.py."""
from collections import namedtuple


def tracker_name(tracker):
    """Return the name of the tracker."""
    return type(tracker).__name__


def is_tracker_present(trackers, tracker):
    """Return true if the tracker is present in list."""
    for i in trackers:
        if tracker_name(tracker) == tracker_name(i):
            return True
    return False


Nose = namedtuple("Nose", "x y")


def add_nose(trackers, x, y):
    """Add nose tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = Nose(x, y)
    if is_tracker_present(trackers, nose):
        raise ValueError("Duplicate value of nose tracker")
    trackers.append(nose)
    
    


LeftEyeInner = namedtuple("LeftEyeInner", "x y")


def add_left_eye_inner(trackers, x, y):
    """Add left_eye_inner tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftEyeInner(x, y)
    if is_tracker_present(trackers, left_eye_inner):
        raise ValueError("Duplicate value of left_eye_inner tracker")
    trackers.append(left_eye_inner)
    
    


LeftEye = namedtuple("LeftEye", "x y")


def add_left_eye(trackers, x, y):
    """Add left_eye tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftEye(x, y)
    if is_tracker_present(trackers, left_eye):
        raise ValueError("Duplicate value of left_eye tracker")
    trackers.append(left_eye)
    
    


LeftEyeOuter = namedtuple("LeftEyeOuter", "x y")


def add_left_eye_outer(trackers, x, y):
    """Add left_eye_outer tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftEyeOuter(x, y)
    if is_tracker_present(trackers, left_eye_outer):
        raise ValueError("Duplicate value of left_eye_outer tracker")
    trackers.append(left_eye_outer)
    
    


RightEyeInner = namedtuple("RightEyeInner", "x y")


def add_right_eye_inner(trackers, x, y):
    """Add right_eye_inner tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightEyeInner(x, y)
    if is_tracker_present(trackers, right_eye_inner):
        raise ValueError("Duplicate value of right_eye_inner tracker")
    trackers.append(right_eye_inner)
    
    


RightEye = namedtuple("RightEye", "x y")


def add_right_eye(trackers, x, y):
    """Add right_eye tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightEye(x, y)
    if is_tracker_present(trackers, right_eye):
        raise ValueError("Duplicate value of right_eye tracker")
    trackers.append(right_eye)
    
    


RightEyeOuter = namedtuple("RightEyeOuter", "x y")


def add_right_eye_outer(trackers, x, y):
    """Add right_eye_outer tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightEyeOuter(x, y)
    if is_tracker_present(trackers, right_eye_outer):
        raise ValueError("Duplicate value of right_eye_outer tracker")
    trackers.append(right_eye_outer)
    
    


LeftEar = namedtuple("LeftEar", "x y")


def add_left_ear(trackers, x, y):
    """Add left_ear tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftEar(x, y)
    if is_tracker_present(trackers, left_ear):
        raise ValueError("Duplicate value of left_ear tracker")
    trackers.append(left_ear)
    
    


RightEar = namedtuple("RightEar", "x y")


def add_right_ear(trackers, x, y):
    """Add right_ear tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightEar(x, y)
    if is_tracker_present(trackers, right_ear):
        raise ValueError("Duplicate value of right_ear tracker")
    trackers.append(right_ear)
    
    


MouthLeft = namedtuple("MouthLeft", "x y")


def add_mouth_left(trackers, x, y):
    """Add mouth_left tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = MouthLeft(x, y)
    if is_tracker_present(trackers, mouth_left):
        raise ValueError("Duplicate value of mouth_left tracker")
    trackers.append(mouth_left)
    
    


MouthRight = namedtuple("MouthRight", "x y")


def add_mouth_right(trackers, x, y):
    """Add mouth_right tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = MouthRight(x, y)
    if is_tracker_present(trackers, mouth_right):
        raise ValueError("Duplicate value of mouth_right tracker")
    trackers.append(mouth_right)
    
    


LeftShoulder = namedtuple("LeftShoulder", "x y")


def add_left_shoulder(trackers, x, y):
    """Add left_shoulder tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftShoulder(x, y)
    if is_tracker_present(trackers, left_shoulder):
        raise ValueError("Duplicate value of left_shoulder tracker")
    trackers.append(left_shoulder)
    
    


RightShoulder = namedtuple("RightShoulder", "x y")


def add_right_shoulder(trackers, x, y):
    """Add right_shoulder tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightShoulder(x, y)
    if is_tracker_present(trackers, right_shoulder):
        raise ValueError("Duplicate value of right_shoulder tracker")
    trackers.append(right_shoulder)
    
    


LeftElbow = namedtuple("LeftElbow", "x y")


def add_left_elbow(trackers, x, y):
    """Add left_elbow tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftElbow(x, y)
    if is_tracker_present(trackers, left_elbow):
        raise ValueError("Duplicate value of left_elbow tracker")
    trackers.append(left_elbow)
    
    


RightElbow = namedtuple("RightElbow", "x y")


def add_right_elbow(trackers, x, y):
    """Add right_elbow tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightElbow(x, y)
    if is_tracker_present(trackers, right_elbow):
        raise ValueError("Duplicate value of right_elbow tracker")
    trackers.append(right_elbow)
    
    


LeftWrist = namedtuple("LeftWrist", "x y")


def add_left_wrist(trackers, x, y):
    """Add left_wrist tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftWrist(x, y)
    if is_tracker_present(trackers, left_wrist):
        raise ValueError("Duplicate value of left_wrist tracker")
    trackers.append(left_wrist)
    
    


RightWrist = namedtuple("RightWrist", "x y")


def add_right_wrist(trackers, x, y):
    """Add right_wrist tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightWrist(x, y)
    if is_tracker_present(trackers, right_wrist):
        raise ValueError("Duplicate value of right_wrist tracker")
    trackers.append(right_wrist)
    
    


LeftPinky = namedtuple("LeftPinky", "x y")


def add_left_pinky(trackers, x, y):
    """Add left_pinky tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftPinky(x, y)
    if is_tracker_present(trackers, left_pinky):
        raise ValueError("Duplicate value of left_pinky tracker")
    trackers.append(left_pinky)
    
    


RightPinky = namedtuple("RightPinky", "x y")


def add_right_pinky(trackers, x, y):
    """Add right_pinky tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightPinky(x, y)
    if is_tracker_present(trackers, right_pinky):
        raise ValueError("Duplicate value of right_pinky tracker")
    trackers.append(right_pinky)
    
    


LeftIndex = namedtuple("LeftIndex", "x y")


def add_left_index(trackers, x, y):
    """Add left_index tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftIndex(x, y)
    if is_tracker_present(trackers, left_index):
        raise ValueError("Duplicate value of left_index tracker")
    trackers.append(left_index)
    
    


RightIndex = namedtuple("RightIndex", "x y")


def add_right_index(trackers, x, y):
    """Add right_index tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightIndex(x, y)
    if is_tracker_present(trackers, right_index):
        raise ValueError("Duplicate value of right_index tracker")
    trackers.append(right_index)
    
    


LeftThumb = namedtuple("LeftThumb", "x y")


def add_left_thumb(trackers, x, y):
    """Add left_thumb tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftThumb(x, y)
    if is_tracker_present(trackers, left_thumb):
        raise ValueError("Duplicate value of left_thumb tracker")
    trackers.append(left_thumb)
    
    


RightThumb = namedtuple("RightThumb", "x y")


def add_right_thumb(trackers, x, y):
    """Add right_thumb tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightThumb(x, y)
    if is_tracker_present(trackers, right_thumb):
        raise ValueError("Duplicate value of right_thumb tracker")
    trackers.append(right_thumb)
    
    


LeftHip = namedtuple("LeftHip", "x y")


def add_left_hip(trackers, x, y):
    """Add left_hip tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftHip(x, y)
    if is_tracker_present(trackers, left_hip):
        raise ValueError("Duplicate value of left_hip tracker")
    trackers.append(left_hip)
    
    


RightHip = namedtuple("RightHip", "x y")


def add_right_hip(trackers, x, y):
    """Add right_hip tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightHip(x, y)
    if is_tracker_present(trackers, right_hip):
        raise ValueError("Duplicate value of right_hip tracker")
    trackers.append(right_hip)
    
    


LeftKnee = namedtuple("LeftKnee", "x y")


def add_left_knee(trackers, x, y):
    """Add left_knee tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftKnee(x, y)
    if is_tracker_present(trackers, left_knee):
        raise ValueError("Duplicate value of left_knee tracker")
    trackers.append(left_knee)
    
    


RightKnee = namedtuple("RightKnee", "x y")


def add_right_knee(trackers, x, y):
    """Add right_knee tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightKnee(x, y)
    if is_tracker_present(trackers, right_knee):
        raise ValueError("Duplicate value of right_knee tracker")
    trackers.append(right_knee)
    
    


LeftAnkle = namedtuple("LeftAnkle", "x y")


def add_left_ankle(trackers, x, y):
    """Add left_ankle tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftAnkle(x, y)
    if is_tracker_present(trackers, left_ankle):
        raise ValueError("Duplicate value of left_ankle tracker")
    trackers.append(left_ankle)
    
    


RightAnkle = namedtuple("RightAnkle", "x y")


def add_right_ankle(trackers, x, y):
    """Add right_ankle tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightAnkle(x, y)
    if is_tracker_present(trackers, right_ankle):
        raise ValueError("Duplicate value of right_ankle tracker")
    trackers.append(right_ankle)
    
    


LeftHeel = namedtuple("LeftHeel", "x y")


def add_left_heel(trackers, x, y):
    """Add left_heel tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftHeel(x, y)
    if is_tracker_present(trackers, left_heel):
        raise ValueError("Duplicate value of left_heel tracker")
    trackers.append(left_heel)
    
    


RightHeel = namedtuple("RightHeel", "x y")


def add_right_heel(trackers, x, y):
    """Add right_heel tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightHeel(x, y)
    if is_tracker_present(trackers, right_heel):
        raise ValueError("Duplicate value of right_heel tracker")
    trackers.append(right_heel)
    
    


LeftFootIndex = namedtuple("LeftFootIndex", "x y")


def add_left_foot_index(trackers, x, y):
    """Add left_foot_index tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = LeftFootIndex(x, y)
    if is_tracker_present(trackers, left_foot_index):
        raise ValueError("Duplicate value of left_foot_index tracker")
    trackers.append(left_foot_index)
    
    


RightFootIndex = namedtuple("RightFootIndex", "x y")


def add_right_foot_index(trackers, x, y):
    """Add right_foot_index tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = RightFootIndex(x, y)
    if is_tracker_present(trackers, right_foot_index):
        raise ValueError("Duplicate value of right_foot_index tracker")
    trackers.append(right_foot_index)
    
    


ClubGrip = namedtuple("ClubGrip", "x y")


def add_club_grip(trackers, x, y):
    """Add club_grip tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = ClubGrip(x, y)
    if is_tracker_present(trackers, club_grip):
        raise ValueError("Duplicate value of club_grip tracker")
    trackers.append(club_grip)
    
    


ClubHeel = namedtuple("ClubHeel", "x y")


def add_club_heel(trackers, x, y):
    """Add club_heel tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = ClubHeel(x, y)
    if is_tracker_present(trackers, club_heel):
        raise ValueError("Duplicate value of club_heel tracker")
    trackers.append(club_heel)
    
    


ClubToe = namedtuple("ClubToe", "x y")


def add_club_toe(trackers, x, y):
    """Add club_toe tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = ClubToe(x, y)
    if is_tracker_present(trackers, club_toe):
        raise ValueError("Duplicate value of club_toe tracker")
    trackers.append(club_toe)
    
    

