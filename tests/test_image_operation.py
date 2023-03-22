'''
Test out cv2 algorithms
'''

from golftracker import image_operation
import numpy as np
import cv2


def test_blank():
    h = w = 100
    frame = np.zeros((h, w, 3), np.uint8)
    canny = image_operation.CannyEdgeDetection()
    f = canny.process(frame)
    assert f.shape == frame.shape
    lst = canny.run([frame])
    assert len(lst) == 1
    assert lst[0].shape == frame.shape


def test_canny_edge_detection():
    detector = image_operation.CannyEdgeDetection()
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    edges = detector.process(img)
    assert edges.shape == (100, 100, 3)
    assert np.all(edges == 0)

def test_hough_line_detector():
    detector = image_operation.HoughLineDetector()
    detector.min_line_length = 1
    detector.max_line_gap = 1
    img = np.zeros((100, 100), dtype=np.uint8)
    img[50:55, 0:100] = 255
    lines = detector.process(img)
    assert len(lines) > 1
    assert lines[0][0] == 0
    assert lines[0][1] == 51
    assert lines[0][2] == 99
    assert lines[0][3] == 51

def test_detect_lines_in_region():
	width, height = 800, 600
	x1, y1 = 0, 0
	x2, y2 = 200, 400
	frame= np.zeros((height, width, 3), np.uint8)
	line_thickness = 2
	img = cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=line_thickness)
	canny_edge_img = image_operation.CannyEdgeDetection().process(img)
	single_channel_canny_img = cv2.cvtColor(canny_edge_img, cv2.COLOR_BGR2GRAY)
	lines = image_operation.HoughLineDetector().process(single_channel_canny_img)	
	assert len(lines) > 0