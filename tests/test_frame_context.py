from frame_context import *

def test_init():
    fc = FrameContext()
    assert len(fc.frame_tracker) > 0
    assert len(fc.msgs) == 0
    