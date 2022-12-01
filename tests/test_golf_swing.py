from golftracker import golf_swing
from golftracker import golf_swing_factory


import numpy as np
import os
import json



def test_null_init():
    gs = golf_swing.GolfSwing(10, 20)
    assert len(gs.mp_pose_frame_landmarks) == 0
    assert gs.height == 10
    assert gs.width == 20

def test_json():
    gs = golf_swing.GolfSwing(height=10, width=20)
    json_str = gs.to_json()
    fmt = json.loads(json_str)
    assert fmt['height'] == 10