#
# Detect the golf club.
# A golf club is a straight line that passed through/close to the wrist vertex.

import numpy as np 
import cv2
import math
import logging

from golftracker import geom
from operator import add

def detect_club_lines(lines, points):
    """Sort the incoming lines in descending probability of being a club."""
    if lines == []:
        return []
    log = logging.getLogger(__name__)

    wrist = points['right_wrist']
    elbow = points['right_elbow']

    log.info(f'Found {len(lines)} lines in the frame')
    wrist_lst = list(map(lambda l: geom.shortest_dist_from_point_to_line(wrist, l), lines))
    elbow_lst = list(map(lambda l: geom.shortest_dist_from_point_to_line(elbow, l), lines))

    dist_lst = list(map(add, wrist_lst, elbow_lst))
    decorated_lst = list(zip(lines, dist_lst))
    decorated_lst.sort(key=lambda l: l[1])

    sorted_lines = [decorated_lst[i][0] for i in range(len(decorated_lst))]
    
    return sorted_lines