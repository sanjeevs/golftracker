'''
Stores the result of the pose model.
'''
from golftracker import gt_const as gt
from collections import Counter

class PoseResult:

    def __init__(self, num_frames):
        self.poses = [gt.GolfPose.Unknown] * num_frames
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

    def get_first_start_pose_frame_idx(self):
        """ Return the first time the start pose is detected.
            Else return None
        """
        start_idx = None
        for i, pose in enumerate(self.poses):
            if pose == gt.GolfPose.RhStart or pose == gt.GolfPose.LhStart:
                start_idx = i
                break
        return start_idx

    def get_last_finish_pose_frame_idx(self):
        """Return the last golf swing finish else return None"""
        finish_idx = None
        for i, pose in enumerate(self.poses):
            if pose == gt.GolfPose.RhFinish or pose == gt.GolfPose.LhFinish:
                finish_idx = i        
        return finish_idx