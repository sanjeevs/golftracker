'''
Detect the club head in the set of lines.
'''
from golftracker import image_operations
from golftracker import geom

def run(lines_lst, pose_results, finger_points, given_club_head_points):
    """
    Comute the list of club head positions in the lines.
    """
    num_frames = len(lines_lst)
    club_head_points = [None] * num_frames

    # Phase 1 : highest priority to manual selected club head points.
    # If current finger position is the same, then use the previous value.
    last_given_finger_point = None
    for idx in range(num_frames):
        if given_club_head_points[idx]:
            club_head_points[idx] = given_club_head_points[idx]
            last_given_finger_point = finger_points[idx]          # Save for next
            last_given_club_head_point = given_club_head_points[idx]
        elif last_given_finger_point:
            curr_finger_point = finger_points[idx]
            movement = geom.length(curr_finger_point, last_given_finger_point)
            print(f">>Frame[{idx}]:Movement={movement}")
            if abs(movement) < 50:  # Hand tuning
                club_head_points[idx] = last_given_club_head_point

    # Phase 2: estimate the points using a linear scale.
    # Phase 2: Select lines that make sense
    for idx in range(num_frames):
        if not club_head_points[idx]:
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

def estimate_club_head(club_head_points):
    """
    Estimate the position of the club head using a linear model.
    """
    num_frames = len(club_head_points)
    est_club_head_points = [None] * num_frames
    lsb_idx = None

    for idx in range(num_frames):
        if club_head_points[idx]:
            if lsb_idx == None:
                lsb_idx = idx
            else:
                msb_idx = idx
                num_segments = msb_idx - lsb_idx - 1
                mid_points = geom.segment_line(club_head_points[lsb_idx],
                                                   club_head_points[msb_idx],
                                                   num_segments)
                for i in range(len(mid_points)):
                    est_club_head_points[lsb_idx + 1 + i] = mid_points[i]
                lsb_idx = None

    return est_club_head_points