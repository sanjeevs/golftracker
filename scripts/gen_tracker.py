""" Generates python code for trackers.
    Replace the tracker.py in the src directory with this file.
"""


header = '''
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
'''


template = '''
{N} = namedtuple("{N}", "x y")


def add_{n}(trackers, x, y):
    """Add {n} tracker to the list.

    :param trackers: A list of trackers.
    :type trackers: list
    :param x: normalized x coordinate.
    :param y: normalized y coordinate
    :return: None
    :raises ValueError: Duplicate value of tracker.
    """
    
    nose = {N}(x, y)
    if is_tracker_present(trackers, {n}):
        raise ValueError("Duplicate value of {n} tracker")
    trackers.append({n})
    
    
'''

print(header)

TRACKERS = ["nose", "left_eye_inner", "left_eye", "left_eye_outer",
            "right_eye_inner", "right_eye", "right_eye_outer",
            "left_ear", "right_ear",
            "mouth_left", "mouth_right",
            "left_shoulder", "right_shoulder",
            "left_elbow", "right_elbow",
            "left_wrist", "right_wrist",
            "left_pinky", "right_pinky",
            "left_index", "right_index",
            "left_thumb", "right_thumb",
            "left_hip", "right_hip",
            "left_knee", "right_knee",
            "left_ankle", "right_ankle",
            "left_heel", "right_heel",
            "left_foot_index", "right_foot_index",
            "club_grip", "club_heel", "club_toe"]

for t in TRACKERS:
    cls = ''.join(word.title() for word in t.split('_'))
    s = template.format(n=t, N=cls)
    print(s)