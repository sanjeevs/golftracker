'''
Detect the club head in the set of lines.
'''
from golftracker import image_operations
from golftracker import geom

def run(lines_lst, pose_results, finger_points, given_club_head_points):
    """
    Comute the list of club head positions in the lines.
    """
    club_head_points = [None] * len(lines_lst) 
    for idx in range(len(lines_lst)):
        if given_club_head_points[idx]:
            club_head_points[idx] = given_club_head_points[idx]
        else:
            pass
            finger_point = finger_points[idx]
            club_line = detect_club_lines(lines_lst[idx], finger_point, pose_results[idx])
            club_head = detect_club_head(club_line, pose_results[idx])
            if club_head:
                club_head_points[idx] = club_head

    return club_head_points


def detect_club_lines(cv2_lines, finger_point, pose_result):
    """
    Return the best estimate of the club line.
    """
    club_lines = [None]
    club_lines = geom.sort_lines_closest_to_point(cv2_lines, finger_point)
    est_slope = 1 # FIXME: pose_result.club_line_slope
    if est_slope:
        club_lines = geom.sort_lines_matching_slope(club_lines, est_slope)

    return club_lines

def detect_club_head(club_line, pose_result):
    """ Detect the positon of the club head."""
    return (0, 0)