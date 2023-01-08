from golftracker import golf_swing
from golftracker import golf_swing_factory
from golftracker import club_detection
from golftracker import gt_const
from golftracker import file_utils

import numpy as np
import os
import json


def test_null_init():
    gs = golf_swing.GolfSwing(10, 20, 30)
    assert gs.height == 10
    assert gs.width == 20
    assert gs.num_frames == 30

def test_video_name():
	gs = golf_swing.GolfSwing(10, 20, 30)
	fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
	gs.set_meta_info(fname)
	# Golfswing stores just the basename. When we reconsitute need to patch the path.
	f = file_utils.search_file(os.path.join('tests', 'assets'), gs.video_fname)
	gs.video_fname = f
	frames = gs.get_video_frames()
	assert len(frames) == 3

