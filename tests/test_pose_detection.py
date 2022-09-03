from golftracker import pose_detection, tracker_utils
import pytest
import cv2
import numpy as np
import sys

def test_main():
    with pytest.raises(SystemExit) as exc:
        pd = pose_detection.main()

def test_null_image():
    null_image = np.zeros((100, 100, 3), dtype=np.uint8)
    trackers = pose_detection.run_mp_pose_on_image(null_image)
    assert trackers == {}

def test_image_1():
    trackers = pose_detection.run_mp_pose_on_image(cv2.imread("tests/images/michelle_wie.png"))
    assert len(trackers) == 33