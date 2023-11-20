from golftracker import club_head_result as ch
import copy


def test_initialization():
    num_frames = 5
    ch_result = ch.ClubHeadResult(num_frames)
    assert len(ch_result.points) == num_frames
    assert all(point is None for point in ch_result.points)

def test_update():
    ch_result = ch.ClubHeadResult(3)
    new_points = ch.ClubHeadResult(3)
    new_points.points = [1, 2, 3]

    ch_result.update(new_points)
    assert ch_result.points == [1, 2, 3]

    new_points.points = [4, None, 6]
    ch_result.update(new_points)
    assert ch_result.points == [4, 2, 6]

def test_reset_and_update():
    ch_result = ch.ClubHeadResult(3)
    new_points = ch.ClubHeadResult(3)
    new_points.points = [1, 2, 3]

    ch_result.update(new_points)

    new_points = ch.ClubHeadResult(3)
    new_points.points = [4, None, 6]
    ch_result.reset_and_update(new_points)
    assert ch_result.points == [4, None, 6]

def test_import_lst1():
    lst = [
        [0, 1, "Label"]
    ]
    ch_result = ch.ClubHeadResult(3)
    ch_result.import_lst(lst)
    assert ch_result.points[0] == (0, 1)
    assert ch_result.points[1] == None
    assert ch_result.points[2] == None
    assert ch_result.algos[0] == "Label"
    assert ch_result.algos[1] == "Invalid"
    lst = [
        [2, 3, "label"]
    ]
    ch_result.import_lst(lst)
    assert ch_result.points[0] == (2, 3)
    assert ch_result.points[1] == None
    assert ch_result.points[2] == None

def test_export_lst1():
    ch_result = ch.ClubHeadResult(3)
    ch_result.points[0] = (0, 1)
    ch_result.algos[0] = "Label"
    headers, lst = ch_result.export_lst()
    assert lst[0] == [0, 1, "Label"]
    assert lst[1] == [0, 0, "Invalid"]
    assert lst[2] == [0, 0, "Invalid"]

