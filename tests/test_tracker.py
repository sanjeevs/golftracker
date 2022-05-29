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