from golftracker import mp_tracker
import json
import pytest

def test_nose():
    trackers = {}
    mp_tracker.add_nose(trackers, 10, 11)
    assert len(trackers) == 1
    assert trackers['nose'].x == 10
    assert trackers['nose'].y == 11
   
def test_multi():
    trackers = {}
    mp_tracker.add_nose(trackers, 1, 2)
    mp_tracker.add_left_foot_index(trackers, 3, 4)
    mp_tracker.add_right_foot_index(trackers, 5, 6)
    assert len(trackers) == 3
    assert trackers['nose'].x == 1
    assert trackers['nose'].y == 2
    assert trackers['left_foot_index'].x == 3
    assert trackers['left_foot_index'].y == 4
    assert trackers['right_foot_index'].x == 5
    assert trackers['right_foot_index'].y == 6

def test_duplicate_nose_exception():
    trackers = {}
    mp_tracker.add_nose(trackers, 10, 11)
    with pytest.raises(ValueError):
        mp_tracker.add_nose(trackers, 12, 13)