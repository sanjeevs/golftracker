"""
Test Media Pipe
----------------
"""
from golftracker import media_pipe_operation as mp 
from mediapipe.framework.formats import landmark_pb2
from golftracker import image_utils
import os
import cv2


def test_null():
    """Test when media pipe fails to detect the human."""
    num_frames = 10
    frames = image_utils.create_blank_frames(num_frames)
    video_landmarks = mp.run(frames)
    assert len(video_landmarks) == num_frames
    assert video_landmarks == [[]] * num_frames

def test_pose1():
    """Test on a single frame that media pipe runs successfully."""
    fname = os.path.join("tests", "assets", "test_pose1.jpg")
    frames = []
    frames.append(cv2.imread(fname))
    video_landmarks = mp.run(frames)
    assert len(video_landmarks) == 1
    assert isinstance(video_landmarks[0], landmark_pb2.NormalizedLandmarkList) == True