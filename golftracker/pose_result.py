'''
Stores the result of the pose model.
'''
from golftracker import gt_const as gt

class PoseResult:

    def __init__(self, num_frames):
        self.poses = [gt.GolfPose.Unknown] * num_frames
        self.pose_sequence = (None, None)  # Start to end pose frames
        self.handed = gt.Handedness.Unknown  # Is it left or right handed.

    def is_valid_swing(self):
        """
        Return true if we detected a valid swing.
        """
        status = False
        if self.pose_sequence[0] is not None and self.pose_sequence[1] is not None:
            num_swing_frames = self.pose_sequence[1] - self.pose_sequence[0]
            if num_swing_frames > 5:  # Arbitary
                status = True

        return status