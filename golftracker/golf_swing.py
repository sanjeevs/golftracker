#
# Root object.
# Constraint: length of frames == length of frame contexts
# Collection of tuples (frame, frame_context)

from .frame_context import *

class GolfSwing:
    def __init__(self, frames):
        self.frames = frames
        self.frame_contexts = [FrameContext()] * len(frames)