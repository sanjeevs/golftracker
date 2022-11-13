#
# Represents the current state of swing processing.
# Aggregate class that encaps frame tracker, msgs and more in future
#
import frame_tracker

class FrameContext:
    def __init__(self):
        self.frame_tracker = frame_tracker.FrameTracker()
        self.msgs = []