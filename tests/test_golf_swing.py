from golftracker import golf_swing
from golftracker import gt_const as gt
from golftracker import file_utils

import numpy as np
import os
import json


def test_null_init():
    video_input = golf_swing.VideoInput(fname="video_fname", size=100,
            scale=1, rotate=0)
    video_spec = golf_swing.VideoSpec(width=10, height=20, num_frames=30, fps=10)
    gs = golf_swing.GolfSwing(video_spec, video_input)
    assert gs.height == 20
    assert gs.width == 10
    assert gs.num_frames == 30
    assert gs.video_input.fname == "video_fname"
    assert gs.get_golf_pose(10) == gt.GolfPose.Unknown
