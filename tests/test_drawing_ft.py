""" Test out drawing the frame tracker. """
import os
import numpy as np
import cv2


from golftracker import visualize, frame_tracker

def test_connections():
	assert visualize.POINTS[12] == "right_shoulder"
	assert visualize.POINTS[17] == "left_pinky"
	assert visualize.POINTS[24] == "right_hip"
	assert visualize.POINTS[28] == "right_ankle"
	assert visualize.POINTS[30] == "right_heel"
	assert len(visualize.POINTS) == 33

	 
def test_ft1_json():
	ft = frame_tracker.FrameTracker()
	ft.fm_json(os.path.join("tests", "assets", "ft1.json"))
	img = np.zeros((500, 500, 3), dtype="uint8")

	visualize.draw_frame_tracker(img, ft) 
	cv2.imwrite("ft1.png", img)