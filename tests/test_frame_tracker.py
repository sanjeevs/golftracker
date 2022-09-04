# Test out the frame tracker

from golftracker import frame_tracker

def test_default():
	ft = frame_tracker.FrameTracker()
	assert len(ft) == 36
	assert ft['nose'] == [0, 0]

def test_nose():
	ft = frame_tracker.FrameTracker()
	ft['nose'] = [0.1, 0.2]
	assert ft['nose'] == [0.1, 0.2]

def test_json():
	json_fname = "test_frame_tracker.json"
	ft = frame_tracker.FrameTracker()
	str1 = ft.to_json_str()
	ft.fm_json_str(str1)
	assert ft['nose'] == [0, 0]