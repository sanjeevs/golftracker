from golfdetection import tracker
import sys
import json

def test_tracker_default():
    t = tracker.Tracker()
    assert t.ball == [None, None]

def test_ball():
    t = tracker.Tracker()
    t.update_ball(10, 20)
    hash = json.loads(t.to_json())
    assert hash['ball'] == [10, 20]

def test_shaft():
    t = tracker.Tracker()
    t.update_shaft(10, 20)
    hash = json.loads(t.to_json())
    assert hash['shaft'] == [10, 20, None, None]
    t.update_shaft(30, 40)
    hash = json.loads(t.to_json())
    assert hash['shaft'] == [10, 20, 30, 40]

def test_load_from_json():
    json_str = '{"ball": [null, null], "shaft": [1117, 1033, 844, 695]}'
    t = tracker.make_from_json(json_str)
    assert t.shaft[0] == 1117
    assert t.shaft[1] == 1033
    assert t.shaft[2] == 844
    assert t.shaft[3] == 695
    assert t.ball[0] == None
    assert t.ball[1] == None

def test_merge_default():
    json_str = '{"ball": [null, null], "shaft": [1117, 1033, 844, 695]}'
    obj = tracker.make_from_json(json_str)
    t = tracker.Tracker()
    t.merge_default(obj)
    assert t.shaft[0] == 1117
    assert t.shaft[1] == 1033
    assert t.shaft[2] == 844
    assert t.shaft[3] == 695
    assert t.ball[0] == None
    assert t.ball[1] == None

def test_merge_no_default():
    t = tracker.Tracker()
    t.update_ball(1, 2)
    t.update_shaft(3, 4)
    t.update_shaft(5, 6)

    json_str = '{"ball": [null, null], "shaft": [1117, 1033, 844, 695]}'
    obj = tracker.make_from_json(json_str)
    t.merge_default(obj)

    assert t.shaft[0] == 3
    assert t.shaft[1] == 4
    assert t.shaft[2] == 5
    assert t.shaft[3] == 6