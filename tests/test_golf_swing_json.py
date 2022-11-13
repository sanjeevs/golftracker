from golftracker import golf_swing_factory
import os
import json


def test_save_json():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_mediapipe(fname)

    json_fname = os.path.join('tests', 'out', 'test_blank_3.json')
    gs.save_to_json(json_fname)

    assert os.path.exists(json_fname)

    gs2 = golf_swing_factory.create_from_json(json_fname)
    assert len(gs2.frame_trackers) == 3

def test_1_json():
    json_fname = os.path.join('tests', 'assets', 'test_1.json')
    gs = golf_swing_factory.create_from_json(json_fname)
    assert len(gs.frame_trackers) == 3
    assert gs.frame_trackers[0]['nose'] == [0.0, 1.0]
    assert gs.frame_trackers[1]['nose'] == [2.0, 3.0]
    assert gs.frame_trackers[2]['nose'] == [4.0, 5.0]