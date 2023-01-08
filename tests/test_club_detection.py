from golftracker import club_detection

def test_null():
    result = club_detection.detect_club_lines([], (1, 2))
    assert result == []

def test_single_line():
    lines = [[1, 2, 3, 4]]
    points = {}
    points['right_wrist'] = (1, 2)
    points['right_elbow'] = (1, 2)
    l = club_detection.detect_club_lines(lines, points)
    assert l[0] == [1, 2, 3, 4]

def test_multi_lines():
    lines = [[1, 2.75, 5, 6], [1, 2.5, 3, 4]]
    points = {}
    points['right_wrist'] = (1, 2)
    points['right_elbow'] = (1, 2)
    l = club_detection.detect_club_lines(lines, points)
    assert l[0] == [1, 2.5, 3, 4]