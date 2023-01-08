#
# Test line detection in frame
from golftracker import image_operation
from golftracker import club_detection
import cv2
import numpy as np

def test_detect_lines_in_region():
	width, height = 800, 600
	x1, y1 = 0, 0
	x2, y2 = 200, 400
	frame= np.zeros((height, width, 3), np.uint8)
	line_thickness = 2
	img = cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=line_thickness)
	canny_edge_img = image_operation.CannyEdgeDetection().process(img)
	single_channel_canny_img = cv2.cvtColor(canny_edge_img, cv2.COLOR_BGR2GRAY)
	lines = image_operation.LineDetector().process(single_channel_canny_img)	
	assert len(lines) > 0