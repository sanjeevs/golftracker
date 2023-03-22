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

def test_multi_lines():
    lines = [[1, 2.75, 5, 6], [1, 2.5, 3, 4]]
    points = {}
    points['right_wrist'] = (1, 2)
    sort_l = geom.sort_lines_closest_to_point(lines, points['right_wrist'])
    assert sort_l[0] == [1, 2.5, 3, 4]
