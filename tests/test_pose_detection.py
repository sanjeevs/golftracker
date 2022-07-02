from golftracker import pose_detection
import pytest
import cv2
import numpy as np
import sys

def test_main():
    with pytest.raises(SystemExit) as exc:
        pd = pose_detection.main()

def test_single_frames_fnames_to_json_fnames():
    frame_files = ["a/b/hello.png"]
    json_files = pose_detection.frame_fnames_to_json_fnames(frame_files, "_mp")
    assert json_files[0] == "a/b/hello_mp.json"

def test_multi_frames_fnames_to_json_fnames():
    frame_files = ["frame_000.png", "/a/b/frame_001.png"]
    json_files = pose_detection.frame_fnames_to_json_fnames(frame_files, "_mp")
    assert len(frame_files) == len(json_files)
    assert json_files[0] == "frame_000_mp.json"
    assert json_files[1] == "/a/b/frame_001_mp.json"


def test_null_image():
    null_image = np.zeros((100, 100, 3), dtype=np.uint8)
    trackers = pose_detection.run_mp_pose_on_image(null_image)
    assert trackers == {}

def test_image_1():
    trackers = pose_detection.run_mp_pose_on_image(cv2.imread("tests/images/michelle_wie.png"))
    assert len(trackers) == 33