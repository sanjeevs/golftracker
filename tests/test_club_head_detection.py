from unittest.mock import Mock
from golftracker import golf_swing_factory
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