from golftracker import geom
from golftracker import image_operations

import numpy as np

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

def test_mask_none():
    height = 100
    width = 200
    blank_frame = np.zeros((height, width, 3), np.uint8)
    mask = image_operations.create_mask(blank_frame, (0, 0, width, height))
    assert np.array_equal(mask, blank_frame)
    # Check if the array memory is different
    blank_frame[0] = (255, 255, 0)
    assert not np.array_equal(mask, blank_frame)

def test_sort_lines_closes_to_pt():
    line1 = [20, 20, 100, 200]
    line2 = [30, 30, 300, 300]
    line3 = [250, 100, 300, 300]
    lines = [line1, line2, line3]
    s0 = geom.sort_lines_closest_to_point(lines, (300, 10), 1)
    assert len(s0) == 0

    s1 = geom.sort_lines_closest_to_point(lines, (300, 10), 100)
    assert len(s1) == 1
    assert s1[0] == [250, 100, 300, 300]

def test_sort_lines_matching_slope():
    line1 = [20, 20, 100, 200]
    line2 = [30, 30, 300, 300]
    line3 = [250, 100, 300, 300]
    lines = [line1, line2, line3]
    s0 = geom.sort_lines_matching_slope(lines, 10, 0)
    assert len(s0) == 0
    s0 = geom.sort_lines_matching_slope(lines, 1, 0)
    assert len(s0) == 1

def test_velocities():
    points = [[203, 436], [200, 433], [200, 432]]
    velocities = geom.compute_velocities(points, 30)
    assert len(velocities) == 2
    print(velocities)