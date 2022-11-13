from golftracker import golf_swing
from golftracker import golf_swing_factory
from golftracker import frame_tracker

import numpy as np
import os
import json



def test_null_init():
    gs = golf_swing.GolfSwing(10, 20)
    assert len(gs.frame_trackers) == 0
    assert gs.height == 10
    assert gs.width == 20

def test_json():
    ft1 = frame_tracker.FrameTracker({'nose': (1.0, 2.0)})
    gs = golf_swing.GolfSwing(10, 20)
    gs.frame_trackers = [ft1]
    json_str = gs.to_json()
    fmt = json.loads(json_str)
    lst = fmt['frames']
    
    assert len(lst) == 1
    assert lst[0]['frame_idx'] == 0
    assert lst[0]['frame_tracker']['nose'] == [1.0, 2.0]
    assert lst[0]['frame_tracker']['left_elbow'] == [0.0, 0.0]