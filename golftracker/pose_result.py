'''
Stores the result of the pose model.
'''
from golftracker import gt_const as gt
from collections import Counter

class PoseResult:

    def __init__(self, num_frames):
        self.poses = [gt.GolfPose.Unknown] * num_frames
        self.sequence = (None, None)  # Start to end pose frames
        self.handed = gt.Handedness.Unknown  # Is it left or right handed.

    def __str__(self):
        poses_str = ''
        cnt = Counter(self.poses)
        sequence_str = f"Seq=[{self.sequence[0]}, {self.sequence[1]}]"
        handed_str = f"{self.handed}"
        return f"Poses:{cnt}, Seq={sequence_str}, {handed_str}"

    def is_valid_swing(self):
        """
        Return true if we detected a valid swing.
        """
        status = False
        if self.sequence[0] is not None and self.sequence[1] is not None:
            num_swing_frames = self.sequence[1] - self.sequence[0]
            if num_swing_frames > 5:  # Arbitary
                status = True

        return status