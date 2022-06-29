from golftracker import tracker
import json
import pytest

def test_nose():
    trackers = []
    tracker.add_nose(trackers, 10, 11)
    assert len(trackers) == 1
    assert trackers[0].x == 10
    assert trackers[0].y == 11
    assert type(trackers[0]).__name__ == "Nose"

def test_duplicate_nose_exception():
    trackers = []
    tracker.add_nose(trackers, 10, 11)
    with pytest.raises(ValueError):
        tracker.add_nose(trackers, 12, 13)