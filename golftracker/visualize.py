"""Draw the line joining the trackers on the frame."""
import cv2

import frame_tracker

POINTS = ["nose", "left_eye_inner", "left_eye", "left_eye_outer", "right_eye_inner",
          "right_eye", "right_eye_outer", "left_ear", "right_ear", "mouth_left",
          "mouth_right", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
          "left_wrist", "right_wrist", "left_pinky", "right_pinky", "left_index",
          "right_index", "left_thumb", "right_thumb", "left_hip", "right_hip",
          "left_knee", "right_knee", "left_ankle", "right_ankle", 
          "left_heel", "right_heel", "left_foot_index", "right_foot_index"
         ]

CONNECTIONS = [(18, 20), (20, 22), (18, 16), (22, 16), (16, 14), (14, 12),
               (12, 24), (24, 26), (26, 28), (28, 32), (28, 30), (32, 30),
               (12, 11), (11, 23), (23, 25), (25, 27), (27, 29), (27, 31), 
               (29, 31), (11, 13), (13, 15), (21, 15), (15, 19), (15, 17), 
               (19, 17), (24, 23), (8, 6), (6, 5), (5, 4), (4, 0),
               (0, 1), (1, 2), (2, 3), (3, 7), (10, 9)]

def matching_line_segments(tracker_name):
    rslt = []
    line_segments = []

    for c in CONNECTIONS:
        segment = (POINTS[c[0]], POINTS[c[1]])
        line_segments.append(segment)

    for segment in line_segments:
        if segment[0] == tracker_name or segment[1] == tracker_name:
            rslt.append(segment)

    return rslt

def valid_line_segments(tracker, segments):
    rslt = []
    for segment in segments:
        if tracker[segment[0]][0] > 0 or tracker[segment[0]][1] > 0:
            if tracker[segment[1]][0] > 0 or tracker[segment[1]][1] > 0:
                rslt.append(segment)
    return rslt


def draw_segment(img, points):
    """ 
    Draw a line on the image given a pair of points.
    Each point is a tuple with x and y coordinate.

    :param img : Image to draw the line on.
    :param points: A starting and end point.
                   Each point has a x, y normalized values.

    :return: Returns the number of lines drawn

    """

    assert(len(points) == 2)

    w, h, _ = img.shape
    start_norm_point  = points[0]
    end_norm_point = points[1]
    
    start_point = (int(start_norm_point[0] * w), int(start_norm_point[1] * h))
    end_point = (int(end_norm_point[0] * w), int(end_norm_point[1] * h))

    cv2.circle(img, start_point, radius=1, color=(0, 0, 255), thickness=-1)
    cv2.circle(img, end_point, radius=1, color=(0, 255, 255), thickness=-1)
    cv2.line(img, start_point, end_point, color=(255, 0, 0), thickness=1)


def draw_frame_tracker(img, tracker):
    """
    Draw the lines for valid trackers on the image.
    """

    segment_pairs = []
    num_lines = 0
    history = []

    for t_name in tracker.keys():
        valid_segments = []

        if tracker[t_name][0] > 0 or tracker[t_name][1] > 0:
            segments = matching_line_segments(t_name)
            valid_segments = valid_line_segments(tracker, segments)

        for segment in valid_segments:
            if segment not in history:
                history.append(segment)
                node_pair = ([tracker[segment[0]], tracker[segment[1]]])
                draw_segment(img, node_pair)
                num_lines += 1

    return num_lines