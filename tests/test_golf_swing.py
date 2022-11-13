from golftracker import golf_swing
from golftracker import golf_swing_factory
from golftracker import frame_tracker

import numpy as np
import os


def test_null_init():
    gs = golf_swing.GolfSwing([])
    assert len(gs.frames) == 0
    assert len(gs.frame_contexts) == 0

def test_blank_video():
    fname = os.path.join("tests", "assets", "test_blank_3.mov")
    gs = golf_swing_factory.create_from_video(fname)
    assert len(gs.frames) == 3
    assert len(gs.frame_contexts) == 3

    # Ensure deep copy of frame contexts
    gs.frame_contexts[0].frame_tracker["nose"] == (1.0, 2.0)
    assert gs.frame_contexts[1].frame_tracker['nose'] == (0, 0)

def test_clone():
    fname = os.path.join("tests", "assets", "test_blank_3.mov")
    gs = golf_swing_factory.create_from_video(fname)
    gs_clone = golf_swing_factory.clone_new_context(gs)

     # Ensure deep copy of frame contexts
    ft1 = frame_tracker.FrameTracker({'nose': (1.0, 2.0)})
    gs.frame_contexts[0].frame_tracker = ft1
    assert gs_clone.frame_contexts[0].frame_tracker['nose'] == (0, 0)
    assert gs_clone.frame_contexts[1].frame_tracker['nose'] == (0, 0)

    ft2 = frame_tracker.FrameTracker({'nose': (3.0, 4.0)})
    gs_clone.frame_contexts[0].frame_tracker = ft2
    assert gs.frame_contexts[0].frame_tracker['nose'] == (1.0, 2.0)
    assert gs_clone.frame_contexts[1].frame_tracker['nose'] == (0, 0)
    