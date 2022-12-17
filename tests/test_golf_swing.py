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
