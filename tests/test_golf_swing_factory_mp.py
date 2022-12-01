from golftracker import golf_swing_factory
import os

def test_create_from_blank_video():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_video(fname)

    assert len(gs.mp_pose_frame_landmarks) == 3