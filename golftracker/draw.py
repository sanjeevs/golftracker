"""Draw utilities for object detection."""

import cv2

def visualize_trackers(frame, trackers):
    height, width, _ = frame.shape 

    x = int(trackers['left_wrist'][0] * width)
    y = int(trackers['left_wrist'][1] * height)
    cv2.circle(frame, (x, y), radius=5, color=(255, 0, 0), thickness=-1)
