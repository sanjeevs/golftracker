import media_pipe_operation as mp
import numpy as np
from frame_context import FrameContext


def test_blank_images():
    blank_frame = np.zeros((100, 100, 3), np.uint8)
    frames = []
    frame_contexts = []

    for _ in range(3):
        frames.append(blank_frame)
        frame_contexts.append(FrameContext())

    mp.run(frames, frame_contexts)
    for fc in frame_contexts:
        for msg in fc.msgs:
            assert "MediaPipe failed" in msg