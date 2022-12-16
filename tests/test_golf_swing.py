from golftracker import golf_swing
from golftracker import golf_swing_factory
from golftracker import gt_const


import numpy as np
import os
import json


def test_null_init():
    gs = golf_swing.GolfSwing(10, 20, 30)
    assert gs.height == 10
    assert gs.width == 20
    assert gs.num_frames == 30


def test_json():
    gs = golf_swing.GolfSwing(height=10, width=20, num_frames=30)
    gs.set_ml_pose(10, gt_const.GolfPose.RhStart, 0.3)
    json_str = gs.to_json()
   
    new_gs = golf_swing_factory.create_from_json(json_str)
    json_str = ""
    gs = None
    assert new_gs.num_frames == 30
