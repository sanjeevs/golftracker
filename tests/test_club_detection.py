from golftracker import club_detection

def test_null():
    result = club_detection.detect_cv2_lines([])
    assert result == []

def test_multi_lines():
    lines = [[1, 2.75, 5, 6], [1, 2.5, 3, 4]]
    points = {}
    points['right_wrist'] = (1, 2)
    sort_l = club_detection.sort_lines_closest_to_point(lines, points['right_wrist'])
    assert sort_l[0] == [1, 2.5, 3, 4]