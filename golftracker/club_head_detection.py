'''
Detect the club head in the frames.
'''
from golftracker import image_operation
from golftracker import pose_context

def run(frames, pose_contexts, finger_points, given_club_head_points):
	"""
	Comute the list of club head positions in the frame.
	"""
	club_head_points = []
	for frame_idx in len(frames):
		if given_club_head_points[frame_idx]:
			club_head_points[frame_idx] = given_club_head_points[frame_idx]
		else:
			finger_point = finger_points[frame_idx]
			club_line = detect_club_lines(frames[frame_idx], finger_point)
			club_head = detect_club_head(club_line, pose_contexts[frame_idx])
			if club_head:
				club_head_points[frame_idx] = club_head

	return club_head_points


def detect_cv2_lines(frame):
	"""
	Detect lines in a frame using cv2 algorithms
	"""
    if len(frame) == 0:
        return []

    canny = image_operation.CannyEdgeDetection()
    line_detector = image_operation.HoughLineDetector()

    canny_img = canny.process(frame)
    single_channel_canny_edges = cv2.cvtColor(canny_img, cv2.COLOR_BGR2GRAY)
    lines = line_detector.process(single_channel_canny_edges)
    return lines

def detect_club_lines(frame, finger_point, pose_context):
	"""
	Return the best estimate of the club line.
	"""
	club_lines = [None]
	cv2_lines = detect_cv2_lines(frame)
	club_lines = image_operation.sort_lines_closest_to_point(cv2_lines, finger_point)
	est_slope = pose_context.club_line_slope
	if est_slope:
		club_lines = image_operation.sort_lines_matching_slope(club_lines, est_slope)

    return club_lines

def detect_club_head(club_line, pose_context):
	""" Detect the positon of the club head."""
	return (0, 0)