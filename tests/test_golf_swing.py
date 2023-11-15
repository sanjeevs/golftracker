from golftracker import golf_swing
from golftracker import gt_const as gt
from golftracker import file_utils
from golftracker import video_utils

import numpy as np
import os
import json


def test_null_init():
    video_input = video_utils.VideoInput(fname="video_fname", size=100)
    video_spec = video_utils.VideoSpec(width=10, height=20, num_frames=30, fps=10,
            scale=100, rotate=0)
    gs = golf_swing.GolfSwing(video_spec, video_input)
    assert gs.video_spec.height == 20
    assert gs.video_spec.width == 10
    assert gs.video_spec.num_frames == 30
    assert gs.video_input.fname == "video_fname"
    assert gs.get_golf_pose(10) == gt.GolfPose.Unknown
