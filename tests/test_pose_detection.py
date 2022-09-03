# Test out google mp api
# Read an image and check that api is working

from golftracker import pose_detection, frame_tracker
import pytest
import cv2
import numpy as np
import sys


def test_main():
    """ No python syntax issues. """
    with pytest.raises(SystemExit) as exc:
        pd = pose_detection.main()


def test_null_image():
    """ Negative test that there is no pose on black image. """
    null_image = np.zeros((100, 100, 3), dtype=np.uint8)
    ft = pose_detection.run_mp_pose_on_image(null_image)
    assert ft['nose'] == (0,0)


def test_image_1():
    """ Test live image. """
    ft = pose_detection.run_mp_pose_on_image(
        cv2.imread("tests/images/michelle_wie.png")
    )
    assert ft['nose'] != (0,0)
    assert ft['club_heel'] == (0, 0)
