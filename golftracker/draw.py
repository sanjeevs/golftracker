"""Draw utilities for object detection."""

import cv2
from golftracker import tracker

def draw_tracker(frame, tracker):
    """Draw the traacker coordinates as circles on the frame."""
    if tracker.ball[0] != None:
        cv2.circle(img=frame, center=(tracker.ball[0], tracker.ball[1]), radius=10, color=(255, 0, 0), thickness=-1)

    if tracker.shaft[0] != None:
        cv2.circle(img=frame, center=(tracker.shaft[0], tracker.shaft[1]), radius=5, color=(0, 255, 0), thickness=-1)

    if tracker.shaft[2] != None:
        cv2.circle(img=frame, center=(tracker.shaft[2], tracker.shaft[3]), radius=5, color=(0, 255, 0), thickness=-1)

def visualize_tracker(frame, tracker_dict):
    if 'ball' in tracker_dict.keys() and tracker_dict['ball'] is not None:
        cv2.circle(img=frame, center=(tracker_dict['ball']), radius=10, color=(255, 0, 0), thickness=-1)

    if 'shaft' in tracker_dict.keys() and tracker_dict['shaft'] is not None:
        cv2.line(img=frame, pt1=(tracker_dict["shaft"][0], tracker_dict["shaft"][1]), \
                 pt2=(tracker_dict["shaft"][2], tracker_dict["shaft"][3]), \
                 color=(0, 255, 0), thickness=3)

