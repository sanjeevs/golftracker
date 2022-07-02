from golftracker import gd_tracker
import json
import pytest

def test_club_toe():
    trackers = {}
    gd_tracker.add_club_toe(trackers, 10, 11)
    assert len(trackers) == 1
    assert trackers['club_toe'].x == 10
    assert trackers['club_toe'].y == 11

def test_club_toe_heel():
    trackers = {}
    gd_tracker.add_club_toe(trackers, 10, 11)
    gd_tracker.add_club_heel(trackers, 12, 13)

    assert len(trackers) == 2
    assert trackers['club_toe'].x == 10
    assert trackers['club_toe'].y == 11
    assert trackers['club_heel'].x == 12
    assert trackers['club_heel'].y == 13