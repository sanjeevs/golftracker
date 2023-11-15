from golftracker import golf_swing_factory
from golftracker import video_utils
from golftracker import gt_const as gt

import os
import cv2
from unittest.mock import Mock

def test_create_from_blank_video():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    frames, video_spec = video_utils.split_video_to_frames(fname)
    video_input = video_utils.VideoInput(fname=fname, size=100)
    gs = golf_swing_factory.create_from_video(video_input, video_spec, frames)
    assert gs.video_spec.height == 100
    assert gs.video_spec.num_frames == 3
    assert gs.video_input.fname == fname
    assert gs.video_input.size == 100

def test_create_from_mock_ml_pose1():
    fname = os.path.join('tests', 'assets', 'test_pose1.jpg')
    frame = cv2.imread(fname)
    gs = golf_swing_factory.create_from_image(fname, frame)
    assert gs.video_spec.height == 339
    assert gs.video_spec.width == 509
    assert gs.video_spec.num_frames == 1