""" Generates python code for google mediapipe trackers.
    Replace the mp_tracker.py in the src directory with this file.
"""
import sys

# List of landmarks from google mediapipe
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
            "left_foot_index", "right_foot_index"]
            

header = '''
""" Auto Generated tracker from script misc/gen_mp_tracker.py.DO NOT HAND EDIT !!"""

from collections import namedtuple
import mediapipe as mp
mp_pose = mp.solutions.pose

'''

template = '''
{N} = namedtuple("{N}", "x y")


def add_{n}(trackers, x, y):
    """Add {n} tracker to the list with normalized coordinates."""
    {n} = {N}(x, y)
    if "{n}" in trackers.keys():
        raise ValueError("Duplicate value of {n} tracker")
    trackers["{n}"] = {n}
    
    
'''

media_pipe = '''
def add_mp_landmarks(trackers, landmark):
    add_{landmark}(trackers, landmark[mp_pose.PoseLandmark.{landmark}].x,
                   landmark[mp_pose.PoseLandmark.{landmark}].y)
                   
{results.pose_landmarks.landmark[mp_pose.PoseLandmark.{landmark}].x * image_width}, '
                      f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.{landmark}].y *

'''

func_call = '''
def add_mp_landmarks(trackers, landmark):
    """Add media pipe landmarks to tracker list. """
'''

func_body = '''
    add_{t}(trackers, landmark[mp_pose.PoseLandmark.{landmark}].x,
                   landmark[mp_pose.PoseLandmark.{landmark}].y)
'''


def print_func():
    trackers = []

    print(header)

    for t in TRACKERS:
        cls = ''.join(word.title() for word in t.split('_'))
        trackers.append(cls)
        s = template.format(n=t, N=cls)
        print(s)

    print(func_call)

    for t in TRACKERS:
        landmark = t.upper()
        s = func_body.format(t=t, landmark=landmark)
        print(s)

    return trackers


def main(fname):
    orig_stdout = sys.stdout
    with open(fname, "w") as fh:
        sys.stdout = fh
        trackers = print_func()
    sys.stdout = orig_stdout

    print("Created the following trackers")
    for idx, t in enumerate(trackers):
        if idx > 0 and idx % 8 == 0:
            print(t)
        else:
            print(t + ", ", end="")



if __name__ == "__main__":
    print(">>Creating google mediapipe trackers in 'mp_tracker.py'")
    main("mp_tracker.py")
    

