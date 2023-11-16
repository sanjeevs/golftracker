from golftracker import club_head_result as ch

def test_initialization():
    num_frames = 5
    club_head = ch.ClubHeadResult(num_frames)
    assert len(club_head.points) == num_frames
    assert all(point is None for point in club_head.points)

def test_update():
    club_head = ch.ClubHeadResult(3)
    new_points = ch.ClubHeadResult(3)
    new_points.points = [1, 2, 3]

    club_head.update(new_points)
    assert club_head.points == [1, 2, 3]

    new_points.points = [4, None, 6]
    club_head.update(new_points)
    assert club_head.points == [4, 2, 6]

def test_reset_and_update():
    club_head = ch.ClubHeadResult(3)
    new_points = ch.ClubHeadResult(3)
    new_points.points = [1, 2, 3]

    club_head.update(new_points)

    new_points = ch.ClubHeadResult(3)
    new_points.points = [4, None, 6]
    club_head.reset_and_update(new_points)
    assert club_head.points == [4, None, 6]
