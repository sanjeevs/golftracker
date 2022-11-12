#
# Convert the frame context to a image frame.
#
import numpy as np
from .frame_tracker import *
import cv2


def run(height, width, frame_contexts):
    """Returns a list of frames with the drawing. """
    frames = []
    for _ in range(len(frame_contexts)):
        frames.append(np.zeros((height, width, 3), np.uint8))

    for idx, fc in enumerate(frame_contexts):
        _draw(frames[idx], fc)

    return frames

def _draw_segment(frame, points):
    """ 
    Draw a line on the image given a pair of points.
    Each point is a tuple with x and y coordinate.

    :param frame : Image to draw the line on.
    :param points: A starting and end point.
                   Each point has a x, y normalized values.

    :return: Returns the number of lines drawn

    """

    assert(len(points) == 2)

    h, w, _ = frame.shape
    start_norm_point  = points[0]
    end_norm_point = points[1]
    start_point = (int(start_norm_point[0] * w), int(start_norm_point[1] * h))
    end_point = (int(end_norm_point[0] * w), int(end_norm_point[1] * h))

    cv2.circle(frame, start_point, radius=5, color=(0, 0, 255), thickness=-1)
    cv2.circle(frame, end_point, radius=5, color=(0, 0, 255), thickness=-1)
    cv2.line(frame, start_point, end_point, color=(255, 0, 0), thickness=3)


def _draw_frame_tracker(frame, frame_tracker):
    """
    Draw the image on the frame.

    >>> _draw_frame_tracker(np.zeros((100, 100, 3), np.uint8), FrameTracker())
    0

    >>> _draw_frame_tracker(np.zeros((100, 100, 3), np.uint8), \
                            FrameTracker({'right_shoulder': (0.1, 0.2), 'left_shoulder': (0.3, 0.4)}))
    1

    """
    segment_pairs = []
    num_lines = 0
    history = []

    for (t_name, point) in frame_tracker:
        valid_segments = []

        if point[0] > 0 or point[1] > 0:
            segments = matching_line_segments(t_name)
            valid_segments = valid_line_segments(frame_tracker, segments)

        for segment in valid_segments:
            if segment not in history:
                history.append(segment)
                node_pair = ([frame_tracker[segment[0]], frame_tracker[segment[1]]])
                _draw_segment(frame, node_pair)
                num_lines += 1

    return num_lines


def create_media_pipe_line_segments():
    """
    Return a list of all the lines that media pipe draws.
    This is a direct translation of the pose landmark model as outlined in
    https://google.github.io/mediapipe/solutions/pose.html

    >>> len(create_media_pipe_line_segments())
    14

    >>> create_media_pipe_line_segments()[0]
    ('right_wrist', 'right_elbow')


    """       
    mp_points = ["nose", "left_eye_inner", "left_eye", "left_eye_outer", "right_eye_inner",
                "right_eye", "right_eye_outer", "left_ear", "right_ear", "mouth_left",
                "mouth_right", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
                "left_wrist", "right_wrist", "left_pinky", "right_pinky", "left_index",
                "right_index", "left_thumb", "right_thumb", "left_hip", "right_hip",
                "left_knee", "right_knee", "left_ankle", "right_ankle", 
                "left_heel", "right_heel", "left_foot_index", "right_foot_index"
                ]

    mp_lines = [(18, 20), (20, 22), (18, 16), (22, 16), (16, 14), (14, 12),
               (12, 24), (24, 26), (26, 28), (28, 32), (28, 30), (32, 30),
               (12, 11), (11, 23), (23, 25), (25, 27), (27, 29), (27, 31), 
               (29, 31), (11, 13), (13, 15), (21, 15), (15, 19), (15, 17), 
               (19, 17), (24, 23), (8, 6), (6, 5), (5, 4), (4, 0),
               (0, 1), (1, 2), (2, 3), (3, 7), (10, 9)]

    rslt = []
    line_segments = []

    for c in mp_lines:
        segment = (mp_points[c[0]], mp_points[c[1]])
        if segment[0] in FrameTracker.Pts and segment[1] in FrameTracker.Pts:
            line_segments.append(segment)

    return line_segments 


def matching_line_segments(tracker_name):
    """ 
    Return a list of all lines that start or end with this tracker name.

    >>> matching_line_segments("left_hip")
    [('left_shoulder', 'left_hip'), ('left_hip', 'left_knee'), ('right_hip', 'left_hip')]


    >>> matching_line_segments("left_shoulder")
    [('right_shoulder', 'left_shoulder'), ('left_shoulder', 'left_hip'), ('left_shoulder', 'left_elbow')]

    """
    rslt = []
    line_segments = create_media_pipe_line_segments()

    for segment in line_segments:
        if segment[0] == tracker_name or segment[1] == tracker_name:
            rslt.append(segment)

    return rslt

def valid_line_segments(frame_tracker, segments):
    """
    Return a list of valid lines to be drawn. 

    >>> valid_line_segments(FrameTracker(), create_media_pipe_line_segments())
    []


    >>> valid_line_segments(FrameTracker({'right_shoulder': (0.1, 0.2), 'left_shoulder': (0.3, 0.4)}),\
                            create_media_pipe_line_segments())
    [('right_shoulder', 'left_shoulder')]

    """
    rslt = []
    for segment in segments:
        # MP has more trackers than we use. so skip the invalid ones.
        if frame_tracker[segment[0]][0] > 0 or frame_tracker[segment[0]][1] > 0:
            if frame_tracker[segment[1]][0] > 0 or frame_tracker[segment[1]][1] > 0:
                rslt.append(segment)

    return rslt