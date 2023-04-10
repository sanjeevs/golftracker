'''
Wrapper around cv2 algorithm.
Keep it generic.
'''

import cv2
import numpy as np
import logging

from golftracker import geom


def detect_cv2_lines(frame):
    """
    Detect lines in a frame using canny edge and line detection.
    """
    if len(frame) == 0:
        return []

    canny = CannyEdgeDetection()
    line_detector = HoughLineDetector()

    canny_img = canny.process(frame)
    single_channel_canny_edges = cv2.cvtColor(canny_img, cv2.COLOR_BGR2GRAY)
    lines = line_detector.process(single_channel_canny_edges)
    return lines


def create_mask(frame, rectangle):
    """
    Create a new frame with only the rectangle visible. 
    Other area is blacked out.
    """
    (x1, y1, x2, y2) = rectangle
    height, width = frame.shape[:2]
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.rectangle(mask, (x1, y1), (x2, y2), (255, 255, 255), -1)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    return result