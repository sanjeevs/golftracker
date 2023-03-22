"""
Unit test golf poses
"""
from golftracker import golf_poses
from golftracker import gt_const as gt

def test_null_get_first_pose():
    assert golf_poses.get_pose_first_start([gt.GolfPose.Unknown]) == None
    assert golf_poses.get_pose_last_finish([gt.GolfPose.Unknown]) == None
 
def test_single_first_pose():
    assert golf_poses.get_pose_first_start([gt.GolfPose.LhStart]) == 0
    assert golf_poses.get_pose_last_finish([gt.GolfPose.LhStart]) == None

def test_single_end_pose():
    assert golf_poses.get_pose_first_start([gt.GolfPose.LhFinish]) == None
    assert golf_poses.get_pose_last_finish([gt.GolfPose.LhFinish]) == 0

def test_simple_pose():
    seq = [gt.GolfPose.Unknown, gt.GolfPose.LhStart, gt.GolfPose.LhFinish]
    assert golf_poses.get_pose_first_start(seq) == 1
    assert golf_poses.get_pose_last_finish(seq) == 2

def test_simple_pose_dup():
    seq = [gt.GolfPose.Unknown, gt.GolfPose.LhStart, gt.GolfPose.LhFinish]
    seq += seq
    assert golf_poses.get_pose_first_start(seq) == 1
    assert golf_poses.get_pose_last_finish(seq) == 5

def test_pose_seq1():
    seq = [gt.GolfPose.Unknown, gt.GolfPose.Unknown, gt.GolfPose.Unknown, gt.GolfPose.RhStart,
           gt.GolfPose.RhStart, gt.GolfPose.RhStart]
    assert golf_poses.get_pose_first_start(seq) == 3
    assert golf_poses.get_pose_last_finish(seq) == None