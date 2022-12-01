from golftracker import geom


def test_gradient():
    pt1 = [0, 0]
    pt2 = [100, -100]

    assert geom.gradient(pt1, pt2) == -1

def test_angle():
    ptA = [10, 20]
    ptB = [30, 20]
    ptC = [15, 25]

    assert geom.acute_angle_degrees(ptA, ptB, ptC) == 45

def test_screen_angle():
    # Screen coordinate system does not seem to matter.
    ptA = [10, -20]
    ptB = [30, -20]
    ptC = [15, -15]

    assert geom.acute_angle_degrees(ptA, ptB, ptC) == 45

def test_length():
    ptA = [10, -20]
    ptB = [30, -20]

    assert geom.length(ptA, ptB) == 20