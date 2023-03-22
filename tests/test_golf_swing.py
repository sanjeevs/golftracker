from golftracker import golf_swing
from golftracker import gt_const as gt
from golftracker import file_utils

import numpy as np
import os
import json


def test_null_init():
    gs = golf_swing.GolfSwing(10, 20, 30,  10, "video_fname", 100)
    assert gs.height == 10
    assert gs.width == 20
    assert gs.num_frames == 30
    assert gs.video_fname == "video_fname"
    assert gs.get_mp_points(10, 100, 100) == {}
    assert gs.get_golf_pose(10) == gt.GolfPose.Unknown
    assert gs.computed_club_head_points == [None] * 30

    gs.set_given_club_head_point(0, (1, 2))
    assert gs.given_club_head_points[0] == (1, 2)
