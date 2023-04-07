'''
Detect the club head in the frames.
'''
from golftracker import image_operations
from golftracker import geom

def run(frames, pose_results, finger_points, given_club_head_points):
    """
    Comute the list of club head positions in the frame.
    """
    club_head_points = [None] * len(frames) 
    for frame_idx in range(len(frames)):
        if given_club_head_points[frame_idx]:
            club_head_points[frame_idx] = given_club_head_points[frame_idx]
        else:
            finger_point = finger_points[frame_idx]
            club_line = detect_club_lines(frames[frame_idx], finger_point, pose_results[frame_idx])
            club_head = detect_club_head(club_line, pose_results[frame_idx])
            if club_head:
                club_head_points[frame_idx] = club_head

    return club_head_points



def detect_club_lines(frame, finger_point, pose_result):
    """
    Return the best estimate of the club line.
    """
    club_lines = [None]
    cv2_lines = image_operations.detect_cv2_lines(frame)
    club_lines = geom.sort_lines_closest_to_point(cv2_lines, finger_point)
    est_slope = 1 # FIXME: pose_result.club_line_slope
    if est_slope:
        club_lines = geom.sort_lines_matching_slope(club_lines, est_slope)

    return club_lines

def detect_club_head(club_line, pose_result):
    """ Detect the positon of the club head."""
    return (0, 0)