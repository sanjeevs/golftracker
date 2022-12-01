from golftracker import golf_swing_factory
import os
import json


def test_save_json():
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_video(fname)

    json_fname = os.path.join('tests', 'out', 'test_blank_3.json')
    gs.save_to_json(json_fname)

    assert os.path.exists(json_fname)

    gs2 = golf_swing_factory.create_from_json(json_fname)
    assert len(gs2.mp_pose_frame_landmarks) == 3

def test_save_test_pose1():
    fname = os.path.join('tests', 'assets', 'test_pose1.jpg')
    gs = golf_swing_factory.create_from_image(fname)

    json_fname = os.path.join('tests', 'out', 'test_pose1.json')
    gs.save_to_json(json_fname)

    assert os.path.exists(json_fname)
    gs2 = golf_swing_factory.create_from_json(json_fname)
    pd = gs2.get_pose_data(0)
    assert len(pd["nose"]) == 2
    assert pd['nose'][0] > (0.2 * gs2.width)
    assert pd["nose"][1] > (0.2 * gs2.height)
   

def test_save_test_fail_pose1():
    fname = os.path.join('tests', 'assets', 'test_fail_pose1.jpg')
    gs = golf_swing_factory.create_from_image(fname)

    json_fname = os.path.join('tests', 'out', 'test_fail_pose1.json')
    gs.save_to_json(json_fname)

    assert os.path.exists(json_fname)
    gs2 = golf_swing_factory.create_from_json(json_fname)
    assert len(gs2.mp_pose_frame_landmarks) == 1  #There is 1 frame
    pd = gs2.get_pose_data(0)
    assert len(pd["nose"]) == 0