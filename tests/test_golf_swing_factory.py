from golftracker import golf_swing_factory
import os

def test_create_from_blank_video():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_video(fname, pose_model = None)
    json_str = gs.to_json()
    assert gs.height == 100
    assert gs.width == 200
    assert gs.num_frames == 3


def test_create_from_blank_json():
    fname = os.path.join('tests', 'assets', 'test_blank_3.json')
    with open(fname, "r") as fh:
        json_str = fh.read()

    gs = golf_swing_factory.create_from_json(json_str)
    assert gs.num_frames == 3
    assert gs.height == 100
    assert gs.width == 200