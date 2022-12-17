from golftracker import golf_swing_factory
import os
import pickle

def test_create_from_blank_video():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_video(fname, pose_model = None)
    assert gs.height == 100
    assert gs.width == 200
    assert gs.num_frames == 3

