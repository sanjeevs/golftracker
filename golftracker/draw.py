"""Draw utilities for object detection."""

import cv2
from golftracker import tracker

def draw_tracker(frame, tracker):
    if tracker.ball[0] != None:
        cv2.circle(img=frame, center=(tracker.ball[0], tracker.ball[1]), radius=10, color=(255, 0, 0), thickness=-1)

    if tracker.shaft[0] != None:
        cv2.circle(img=frame, center=(tracker.shaft[0], tracker.shaft[1]), radius=5, color=(0, 255, 0), thickness=-1)

    if tracker.shaft[2] != None:
        cv2.circle(img=frame, center=(tracker.shaft[2], tracker.shaft[3]), radius=5, color=(0, 255, 0), thickness=-1)