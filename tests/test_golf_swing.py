from golf_swing import *
import numpy as np


def test_null_init():
    gs = GolfSwing([])
    assert len(gs.frames) == 0
    assert len(gs.frame_contexts) == 0

def test_init():
    blank_frame = np.zeros((100, 100, 3), np.uint8)
    frames = [blank_frame] * 3
    gs = GolfSwing(frames)
    assert len(gs.frames) == 3
    assert len(gs.frame_contexts) == 3