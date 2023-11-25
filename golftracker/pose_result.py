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
        start_idx = self.get_first_start_pose_frame_idx()
        end_idx = self.get_last_finish_pose_frame_idx()
        sequence_str = f"Seq=[{start_idx}, {end_idx}]"
        handed_str = f"{self.handed}"
        return f"Poses:{cnt}, Seq={sequence_str}, {handed_str}"

    def is_valid_swing(self):
        """
        Return true if we detected a valid swing.
        """
        status = False
        start_idx = self.get_first_start_pose_frame_idx()
        end_idx = self.get_last_finish_pose_frame_idx()
        if start_idx is not None and end_idx is not None:
            num_swing_frames = end_idx - start_idx
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

    def serialize(self):
        """
        Serialize the object to a JSON-compatible format.
        """
        return {
            "poses": [pose.name for pose in self.poses],  # Convert Enum members to their names
            "handed": self.handed.name  # Convert the Enum member to its name
        }