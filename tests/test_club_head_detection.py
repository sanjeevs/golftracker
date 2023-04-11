from unittest.mock import Mock
from golftracker import golf_swing_factory
from golftracker import club_head_detection as ch
import os
import cv2

def test_club_head_detection():
    fname = os.path.join('tests', 'assets', 'test_pose1.jpg')
   
    gs = golf_swing_factory.create_from_image(fname, None)
    gs.set_given_club_head_point(0, (1, 2))
    frame = cv2.imread(fname)
    assert len(gs.given_club_head_points) == 1
    gs.run_club_head_detection([frame])
    assert gs.computed_club_head_points[0] == (1, 2)

def test_null_estimate():
	club_head_points = [(0, 0), (100, 100)]
	est_head_points = ch.estimate_club_head(club_head_points)
	assert est_head_points == [None, None]

def test_single_estimate():
	club_head_points = [(0, 0), None, (100, 100)]
	est_head_points = ch.estimate_club_head(club_head_points)
	assert est_head_points == [None, (50, 50), None]

def test_double_estimate():
	club_head_points = [(0, 0), None, None, (100, 100)]
	est_head_points = ch.estimate_club_head(club_head_points)
	assert est_head_points == [None, (33, 33), (66, 66), None]