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
            if abs(movement) < 50:  # Hand tuning
                club_head_points[idx] = last_given_club_head_point

    # Phase 2: estimate the points using a linear scale.
    est_club_head_points = estimate_club_head(club_head_points)

    # Phase 3: Prioritze the lines detected based on estimate.
    for idx in range(num_frames):
        if est_club_head_points[idx]:
            finger_point = finger_points[idx]
            est_ch_point = est_club_head_points[idx]
            club_lines = detect_club_lines(lines_lst[idx], finger_point, est_ch_point)
            if len(club_lines) > 0:
                club_head = (club_lines[0][2], club_lines[0][3])
                club_head_points[idx] = club_head

    return club_head_points


def detect_club_lines(cv2_lines, finger_point, est_ch_point):
    """
    Return the best estimate of the club line.
    """
    est_slope = geom.gradient(finger_point, est_ch_point)
    club_lines = [None]
    club_lines = geom.sort_lines_closest_to_point(cv2_lines, est_ch_point)
    club_lines = geom.sort_lines_closest_to_point(club_lines, finger_point)
    club_lines = geom.sort_lines_matching_slope(club_lines, est_slope)

    return club_lines


def estimate_club_head(club_head_points):
    """
    Estimate the position of the missing club head using a linear model.

    >>> estimate_club_head([(0, 0), None, (100, 100), None, (200, 200)])
    [None, (50, 50), None, (150, 150), None]
    
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
                lsb_idx = msb_idx

    return est_club_head_points