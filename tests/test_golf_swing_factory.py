from golftracker import golf_swing_factory
from golftracker import video_utils
import os
import pickle

def test_create_from_blank_video():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    (frames, _) = video_utils.split_video_to_frames(fname)
    gs = golf_swing_factory.create_from_frames(fname, frames, pose_model = None)
    assert gs.height == 100
    assert gs.width == 200
    assert gs.num_frames == 3

