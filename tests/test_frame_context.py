from golftracker import frame_context, frame_tracker
import copy


def test_init():
    fc = frame_context.FrameContext()
    assert len(fc.frame_tracker) > 0
    assert len(fc.msgs) == 0

def test_deepcopy():
    fc1 = frame_context.FrameContext()
    fc2 = copy.deepcopy(fc1)

    ft1 = frame_tracker.FrameTracker({'club_grip' : (1, 1)})
    fc1.frame_tracker = ft1

    assert fc2.frame_tracker['club_grip'] == (0, 0)
    