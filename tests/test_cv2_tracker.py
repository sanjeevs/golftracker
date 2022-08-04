from golftracker import obj_tracking as ot
import pytest
import numpy as np
import cv2


def test_valid_init():
    algos = ["kcf", "boosting", "mil", "tld", "medianflow", "mosse"]
    for a in algos:
        obj = ot.ObjTracking(a)
        assert obj is not None


def test_invalid_init():
    with pytest.raises(ValueError):
        ot.ObjTracking("x")

def test_null_tracking():
    """Detect no changes if nothing in the image is changing."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    algos = ["kcf", "tld", "medianflow"]
    for a in algos:
        tk = ot.ObjTracking(a)
        tk.add(img, [10, 20, 40, 50])
        for _ in range(10):
            box = tk.update(img)
            if box:
                assert box == [(10, 20, 40, 50)]

def test_static_circle_tracking():
    """Detect a stationary circle of red color on a black image. """
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    start_pt = (10, 20)
    end_pt = (30, 40)
    color = (255, 0, 0)
    thickness = 2
    img1 = cv2.rectangle(img, start_pt, end_pt, color, thickness)
    algos = ["kcf", "medianflow"]
    for a in algos:
        tk = ot.ObjTracking(a)
        bbox = [start_pt[0], start_pt[1], end_pt[0], end_pt[1]]
        tk.add(img, bbox)
        for _ in range(10):
            box = tk.update(img)
            assert box == [(start_pt[0], start_pt[1], end_pt[0], end_pt[1])]