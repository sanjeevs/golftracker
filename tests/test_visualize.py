# Test out visualize

from golftracker import visualize
from golftracker import frame_tracker
import numpy as np


def test_matching_line_segment():
	segments = visualize.matching_line_segments("left_shoulder")
	assert len(segments) > 0

def test_default_valid_line_segments():
	ft = frame_tracker.FrameTracker()
	segments = visualize.matching_line_segments("left_shoulder")
	rslt = visualize.valid_line_segments(ft, segments)
	assert len(rslt) == 0

def test_invalid_line_segments():
	ft = frame_tracker.FrameTracker()
	segments = visualize.matching_line_segments("left_shoulder")
	ft["left_shoulder"] = [0.1, 0]
	rslt = visualize.valid_line_segments(ft, segments)
	assert len(rslt) == 0

def test_valid_line_segments():
	ft = frame_tracker.FrameTracker()
	segments = visualize.matching_line_segments("left_shoulder")
	ft["left_shoulder"] = [0.1, 0]
	ft["right_shoulder"] = [0.2, 0]
	rslt = visualize.valid_line_segments(ft, segments)
	assert len(rslt) == 1

def test_default():
	ft = frame_tracker.FrameTracker()
	img = None
	n = visualize.draw_frame_tracker(img, ft)
	assert n == 0

def test_shoulder():
	ft = frame_tracker.FrameTracker()
	ft["left_shoulder"] = [0.1, 0.2]
	ft["right_shoulder"] = [0.3, 0.4]
	img = np.zeros((500, 500, 1), dtype="uint8")
	n = visualize.draw_frame_tracker(img, ft)
	assert n == 1

def test_hip():
	ft = frame_tracker.FrameTracker()
	ft["left_hip"] = [0.1, 0.2]
	ft["right_hip"] = [0.3, 0.4]
	img = np.zeros((500, 500, 1), dtype="uint8")
	n = visualize.draw_frame_tracker(img, ft)
	assert n == 1
