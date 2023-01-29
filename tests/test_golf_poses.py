from golftracker import golf_poses
from golftracker import gt_const as gt


def test_poses():
    gp = golf_poses.GolfPoses()
    gp.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)
    gp.set_golf_pose(4, gt.GolfPose.LhStart, 0.9)

    pose = gp.get_golf_pose(0)
    assert pose == gt.GolfPose.RhStart
    prob = gp.get_golf_pose_prob(0)
    assert prob == 0.7

    pose = gp.get_golf_pose(4)
    assert pose == gt.GolfPose.LhStart
    prob = gp.get_golf_pose_prob(4)
    assert prob == 0.9


def test_frame_poses():
    gp = golf_poses.GolfPoses()
    gp.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)
    gp.set_golf_pose(1, gt.GolfPose.LhStart, 0.8)
    gp.set_golf_pose(5, gt.GolfPose.RhStart, 0.9)

    frames = gp.get_pose_frames(gt.GolfPose.RhStart)
    assert len(frames) == 2
    assert frames[0] == 0
    assert frames[1] == 5


def test_pose_null_seq1():
    gp = golf_poses.GolfPoses()
    gp.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)

    gp_seq = gp.get_rh_pose_sequence()
    assert gp_seq == (0, 0)


def test_pose_seq1():
    gp = golf_poses.GolfPoses()
    gp.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)
    gp.set_golf_pose(10, gt.GolfPose.RhTop, 0.8)
    gp.set_golf_pose(20, gt.GolfPose.RhStart, 0.9)
    gp.set_golf_pose(30, gt.GolfPose.RhFinish, 0.9)

    gp_seq = gp.get_rh_pose_sequence()
    assert gp_seq == (0, 30)

def test_pose_seq2():
    gp = golf_poses.GolfPoses()
    gp.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)
    gp.set_golf_pose(10, gt.GolfPose.RhTop, 0.8)
    gp.set_golf_pose(20, gt.GolfPose.RhStart, 0.9)
    gp.set_golf_pose(30, gt.GolfPose.RhFinish, 0.9)
    gp.set_golf_pose(40, gt.GolfPose.RhFinish, 0.9)
    gp.set_golf_pose(50, gt.GolfPose.RhFinish, 0.9)
    gp_seq = gp.get_rh_pose_sequence()
    assert gp_seq == (0, 50)