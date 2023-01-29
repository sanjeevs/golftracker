'''
Handle all the processing related to golf poses.
'''
from golftracker import gt_const as gt


class GolfPoses:
    def __init__(self):
        self.golf_poses = {}

    def set_golf_pose(self, frame_idx, golf_pose, prob):
        self.golf_poses[frame_idx] = (golf_pose, prob)

    def get_golf_pose(self, frame_idx):
        if frame_idx in self.golf_poses.keys():
            return self.golf_poses[frame_idx][0]
        else:
            return gt.GolfPose.Unknown

    def get_golf_pose_prob(self, frame_idx):
        if frame_idx in self.golf_poses.keys():
            return self.golf_poses[frame_idx][1]
        else:
            return 0.0

    def get_pose_frames(self, golf_pose):
        lst = []
        for frame_idx in self.golf_poses.keys():
            if self.get_golf_pose(frame_idx) == golf_pose:
                lst.append(frame_idx)
        return lst
 
    def get_pose_first_start(self, pose):
        """ Return the first time the start pose is detected.
            Else return 0
        """
        start_idx = 0
        for i in self.golf_poses.keys():
            if (
                self.golf_poses[i][0] == pose
            ):
                start_idx = i
                break
        return start_idx

    def get_rh_pose_first_start(self):
        return self.get_pose_first_start(gt.GolfPose.RhStart)

    def get_pose_last_finish(self, pose):
        """Return the last golf swing finish else return last idx"""
        finish_idx = 0
        for i in self.golf_poses.keys():
            if (
                self.golf_poses[i][0] == pose
            ):
                finish_idx = i
            
        return finish_idx

    def get_rh_pose_last_finish(self):
        return self.get_pose_last_finish(gt.GolfPose.RhFinish)

    def get_rh_pose_sequence(self):
        return (self.get_rh_pose_first_start(), self.get_rh_pose_last_finish())

    def get_lh_pose_first_start(self):
        return self.get_pose_first_start(gt.GolfPose.LhStart)

    def get_lh_pose_last_finish(self):
        return self.get_pose_last_finish(gt.GolfPose.LhFinish)

    def get_lh_pose_sequence(self):
        return (self.get_lh_pose_first_start(), self.get_lh_pose_last_finish())
