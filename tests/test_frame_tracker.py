from golftracker.frame_tracker import *

NUM_TRACKERS = 22

def test_empty_init():
    ft = FrameTracker()
    assert len(ft) == NUM_TRACKERS
    assert ft['left_heel'] == (0.0, 0.0)

def test_value_init():
    values = {'nose' : (1.2, 1.4), 'club_grip': (3.1, 3.4)}
    ft = FrameTracker(values)
    assert len(ft) == NUM_TRACKERS
    assert ft['nose'] == (1.2, 1.4)
    assert ft['club_grip'] == (3.1, 3.4)

def test_equality():
    ft1 = FrameTracker()
    ft2 = FrameTracker()
    assert ft1 == ft2

def test_equality_zero():
    ft1 = FrameTracker()
    ft2 = FrameTracker({"nose" : (0, 0)})
    assert ft1 == ft2

def test_ne_key():
    ft1 = FrameTracker({'club_grip' : (1, 1)})
    ft2 = FrameTracker({"nose" : (1, 1)})
    assert ft1 != ft2

def test_ne():
    ft1 = FrameTracker()
    ft2 = FrameTracker({"nose": (1, 0)})
    assert ft1 != ft2

def test_hash():
    rslt = {}
    ft = FrameTracker()
    rslt[ft] = 1
    assert len(rslt) == 1

def test_subsume1():
    ft1 = FrameTracker({'club_grip' : (1, 1)})
    ft2 = FrameTracker({"nose" : (2, 2)})
    ft = ft1.subsume(ft2)
    for (t, value) in ft:
        if t == "club_grip":
            assert ft[t] == (1, 1)
        elif t == "nose":
            assert ft[t] == (2, 2)
        else:
            assert ft[t] == (0, 0)

def test_update1():
    ft1 = FrameTracker({'club_grip' : (1, 1)})
    ft2 = FrameTracker({"nose" : (2, 2)})
    ft = ft1.update(ft2)
    for (t, value) in ft:
        if t == "club_grip":
            assert ft[t] == (1, 1)
        elif t == "nose":
            assert ft[t] == (2, 2)
        else:
            assert ft[t] == (0, 0)

def test_subsume2():
    ft1 = FrameTracker({'club_grip' : (1, 1)})
    ft2 = FrameTracker({"club_grip" : (2, 2)})
    ft = ft1.subsume(ft2)
    for (t, value) in ft:
        if t == "club_grip":
            assert ft[t] == (1, 1)
        else:
            assert ft[t] == (0, 0)

def test_update2():
    ft1 = FrameTracker({'club_grip' : (1, 1)})
    ft2 = FrameTracker({"club_grip" : (2, 2)})
    ft = ft1.update(ft2)
    for (t, value) in ft:
        if t == "club_grip":
            assert ft[t] == (2, 2)
        else:
            assert ft[t] == (0, 0)