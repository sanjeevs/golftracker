from golftracker import club_head_detector
from unittest.mock import Mock

def test_basic():
    gs = Mock()
    gs.num_frames = 10
    params = Mock()
    ch_det = club_head_detector.ClubHeadDetector(gs, params)
    assert ch_det.screen_point(0) == None