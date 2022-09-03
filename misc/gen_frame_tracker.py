""" Generates python code for google mediapipe trackers.
    Replace the mp_tracker.py in the src directory with this file.
"""
import sys

# List of landmarks from google mediapipe
MP_TRACKERS = ["nose", "left_eye_inner", "left_eye", "left_eye_outer",
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
            

CLUB_TRACKERS = ["club_grip", "club_heel", "club_toe"]

header = '''
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

        # Initialize all the trackers with default 0, 0 coord'''

init_body = '''
        self.names.append("{n}")'''

class_body = '''
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
'''

mp_call = '''
    def set_mp_trackers(self, landmark):
        """Add media pipe landmarks to tracker list. """ 
'''

mp_body = '''
        self.trackers["{t}"] = (landmark[mp_pose.PoseLandmark.{landmark}].x,
                                landmark[mp_pose.PoseLandmark.{landmark}].y)
'''


def print_func():
    print(header)
    for t in (MP_TRACKERS + CLUB_TRACKERS):
        s = init_body.format(n=t)
        print(s, end="")

    print()
    print(class_body, end="")

    print(mp_call, end="")
    for mp in MP_TRACKERS:
        s = mp_body.format(landmark=mp.upper(), t=mp)
        print(s, end="")

def main(fname):
    orig_stdout = sys.stdout
    with open(fname, "w") as fh:
        sys.stdout = fh
        print_func()
    sys.stdout = orig_stdout


if __name__ == "__main__":
    print(">>Creating class in 'frame_tracker.py'")
    main("frame_tracker.py")
    

