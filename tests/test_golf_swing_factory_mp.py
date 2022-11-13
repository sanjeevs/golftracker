from golftracker import golf_swing_factory
import os

def test_create_from_mediapipe():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_mediapipe(fname)

    assert len(gs.frame_trackers) == 3