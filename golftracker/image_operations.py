'''
Wrapper around cv2 algorithm.
Keep it generic.
'''

import cv2
import numpy as np
import logging

from golftracker import geom

RED = (0, 0, 255)
YELLOW = (0, 255, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

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

def draw_lines(frame, lines):
    """
    Draw the lines on the frame.
    The order of color is Red, Yellow, Green, Blue...
    """
    for i, line in enumerate(lines):
        if i == 0:
            cv2.line(frame, (line[0], line[1]), (line[2], line[3]), color=RED, thickness=3)
        elif i == 1:
            cv2.line(frame, (line[0], line[1]), (line[2], line[3]), color=YELLOW, thickness=3)
        elif i == 2:
            cv2.line(frame, (line[0], line[1]), (line[2], line[3]), color=GREEN, thickness=3)
        else:
            cv2.line(frame, (line[0], line[1]), (line[2], line[3]), color=GREY, thickness=1)