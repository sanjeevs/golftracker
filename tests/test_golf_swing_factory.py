from golftracker import golf_swing_factory
from golftracker import video_utils
from golftracker import gt_const as gt

import os
import pickle
from unittest.mock import Mock

def test_create_from_blank_video():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    ml_model = None
   
    gs = golf_swing_factory.create_from_video(fname, ml_model)
    assert gs.height == 100
    assert gs.num_frames == 3
    assert gs.video_fname == fname

    # Becasuse we are using a mock, the return value 
    for i in range(3):
            assert gs.get_golf_pose(i) == gt.GolfPose.Unknown
    mp_points = gs.get_mp_points(0)
    assert mp_points == {}

def test_create_from_mock_ml_pose1():
    fname = os.path.join('tests', 'assets', 'test_pose1.jpg')
    ml_model = Mock()
    ml_model.predict.return_value = ['RhStart']
    ml_model.predict_proba.return_value = [[0.1, 0.2, 0.9]]

    gs = golf_swing_factory.create_from_image(fname, ml_model)
    assert gs.height == 339
    assert gs.width == 509
    assert gs.num_frames == 1
    assert gs.get_golf_pose(0) == gt.GolfPose.RhStart