""""
Test the storage of mediapipe results.
"""
from golftracker import media_pipe_landmarks
from golftracker import gt_const as gt

def test_null():
	mp = media_pipe_landmarks.MediaPipeLandmarks(0)
	assert mp.video_landmarks == []

def test_single_entry():
	mp_results = media_pipe_landmarks.MediaPipeLandmarks(1)
	lst = [1.0] * gt.num_mp_landmarks() * 4
	normalized_landmarks = gt.create_pb_normalized_landmarks(lst)
	mp_results.set_mp_results([normalized_landmarks])
	assert mp_results.get_norm_points_dict(0)['nose'] == [1, 1]