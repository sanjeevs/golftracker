#
# Detect the golf club.
# A club is a straight line, from the grip to the club head.
# The grip is where the wrist is. Detecting the club head is harder.

# SAP1:
# Given the postion of the club from the user, compute the rest of the positions.
# For this I can use the position in start_port and finish_pose, to compute the rest.
# The next step is to use line detection to find lines that are closest to the computed postion.
# Adjust the computed value to the new detected position.

import numpy as np 
import cv2
import math
import logging


from golftracker import geom
from golftracker import image_operation

from operator import add

def computed_golf_lines(golf_swing):
    """ Compute the club lines from golden value. """
    lines = {}
    for frame_idx in range(golf_swing.num_frames):
        line = golf_swing.get_club_line(frame_idx)
        if line:
            lines[frame_idx] = line

    return lines

def run(golf_swing, video_frames):
    """ Find the golf club line for each of the frames.
        Look at the computed lines and cv2 detection of lines.
        Choose the most appropriate.
    """
    club_lines = {}
    prev_club_head = None
    log = logging.getLogger(__name__)
    computed_lines = computed_golf_lines(golf_swing)

    for frame_idx, frame in enumerate(video_frames):
        if frame_idx in computed_lines.keys():
            club_lines[frame_idx] = computed_lines[frame_idx]
        else:
            lines = detect_cv2_lines(frame)
            points = golf_swing.get_screen_points(frame_idx)
            lines = sort_lines_closest_to_point(lines, points['right_elbow'])
            lines = sort_lines_closest_to_point(lines, points['right_wrist'])
            club_lines[frame_idx] = lines[0]

    return club_lines


def detect_cv2_lines(frame):
    if not frame:
        return []
        
    canny = image_operation.CannyEdgeDetection()
    line_detector = image_operation.HoughLineDetector()

    canny_img = canny.process(frame)
    single_channel_canny_edges = cv2.cvtColor(canny_img, cv2.COLOR_BGR2GRAY)
    lines = line_detector.process(single_channel_canny_edges)
    return lines


def sort_lines_closest_to_point(lines, point):
    """Sort the incoming lines in descending probability of being a club."""
    if lines == []:
        return []
    
    dist_lst = list(map(lambda l: geom.shortest_dist_from_point_to_line(point, l), lines))
    decorated_lst = list(zip(lines, dist_lst))    
    decorated_lst.sort(key=lambda l: l[1])
    
    sorted_lines = [decorated_lst[i][0] for i in range(len(decorated_lst))]
    
    return sorted_lines