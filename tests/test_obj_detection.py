from golftracker import obj_tracking as ob
import pytest
import numpy as np
import cv2


def test_valid_init():
    algos = ["kcf", "boosting", "mil", "tld", "medianflow", "mosse"]
    for a in algos:
        obj = ob.ObjTracking(a)
        assert obj is not None


def test_invalid_init():
    with pytest.raises(ValueError):
        ob.ObjTracking("x")

def test_null_tracking():
    """Find algos that don't do false matches for no changes."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    algos = ["kcf", "tld", "medianflow"]
    for a in algos:
        tk = ob.ObjTracking(a)
        tk.setup(img, [10, 20, 40, 50])
        for _ in range(10):
            box = tk.update(img)
            if box:
                assert box == [(10, 20, 40, 50)]

def test_circle_tracking():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    start_pt = (10, 20)
    end_pt = (30, 40)
    color = (255, 0, 0)
    thickness = 2
    img1 = cv2.rectangle(img, start_pt, end_pt, color, thickness)
    algos = ["kcf", "medianflow"]
    for a in algos:
        tk = ob.ObjTracking(a)
        bbox = [start_pt[0], start_pt[1], end_pt[0], end_pt[1]]
        tk.setup(img, bbox)
        for _ in range(10):
            box = tk.update(img)
            assert box == [(start_pt[0], start_pt[1], end_pt[0], end_pt[1])]
