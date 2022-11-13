from golftracker import frame_context

def test_init():
    fc = frame_context.FrameContext()
    assert len(fc.frame_tracker) > 0
    assert len(fc.msgs) == 0
    