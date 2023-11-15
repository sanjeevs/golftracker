from golftracker import club_head_result as ch

def test_initialization():
    num_frames = 5
    chr = ch.ClubHeadResult(num_frames)
    assert len(chr.points) == num_frames
    assert all(point is None for point in chr.points)

def test_merge_with_preserve():
    chr = ch.ClubHeadResult(3)
    new = ch.ClubHeadResult(3)
    new.points = [1, None, 3]
    chr.merge_with_preserve(new)
    assert chr.points == [1, None, 3]

    # Testing preservation of non-None values
    new = ch.ClubHeadResult(3)
    new.points = [None, 4, None]
    chr.merge_with_preserve(new)
    assert chr.points == [1, 4, 3]

def test_replace_all():
    chr = ch.ClubHeadResult(3)
    new = ch.ClubHeadResult(3)
    new.points = [1, 2, 3]
    chr.replace_all(new)
    assert chr.points == [1, 2, 3]

    new.points = [4, 5, 6]
    chr.replace_all(new)
    assert chr.points == [4, 5, 6]

def test_reset_and_update():
    chr = ch.ClubHeadResult(3)
    chr.reset_and_update([1, 2, 3])
    assert chr.points == [1, 2, 3]

    # Test resetting and updating with a different length list
    chr.reset_and_update([4, 5])
    assert chr.points == [4, 5]
