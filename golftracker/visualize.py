"""Draw the line joining the trackers on the frame."""
import cv2

from golftracker import frame_tracker

LINE_SEGMENTS = (
    ("left_shoulder", "right_shoulder"),
    ("right_shoulder", "right_hip"),
    ("right_hip", "right_knee"),
    ("right_knee", "right_ankle"),
    ("right_ankle", "right_foot_index"),
    ("right_ankle", "right_heel"),
    ("right_heel", "right_foot_index")
)

def matching_line_segments(tracker_name):
    rslt = []
    for segment in LINE_SEGMENTS:
        if segment[0] == tracker_name or segment[1] == tracker_name:
            rslt.append(segment)

    return rslt

def valid_line_segments(tracker, segments):
    rslt = []
    for segment in segments:
        if tracker[segment[0]][0] > 0 or tracker[segment[0]][1] > 0:
            if tracker[segment[1]][0] > 0 or tracker[segment[1]][1]:
                rslt.append(segment)
    return rslt


def draw_segment(img, node_pair):
    """ 
    Draw a line on the image given a pair of points.
    Each point is a tuple with x and y coordinate.
    """

    assert(len(node_pair) == 2)

    w, h, _ = img.shape
    start_node  = node_pair[0]
    end_node = node_pair[1]

    print(f">>NodePair={node_pairs}")
    
    start_point = (int(start_node[0] * w), int(start_node[1] * h))
    end_point = (int(end_node[0] * w), int(end_node[1] * h))

   
    print(f"Start={start_point}, End={end_point}")
    cv2.line(img, start_point, end_point, color=(255, 0, 0), thickness=2)


def draw_trackers(img, tracker):
    segment_pairs = []
    num_lines = 0
    history = []

    for t_name in tracker.keys():
        valid_segments = []

        if tracker[t_name][0] > 0 or tracker[t_name][1] > 0:
            segments = matching_line_segments(t_name)
            valid_segments = valid_line_segments(ft, segments)

        for segment in valid_segments:
            if segment not in history:
                history.append(segment)
                node_pair = ([tracker[segment[0]], tracker[segment[1]]])
                draw_segment(img, node_pair)
                num_lines += 1

    return num_lines