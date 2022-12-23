from golftracker import golf_data
from golftracker import gt_const as gt

def test_poses():
    gd = golf_data.GolfData(10)
    gd.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)
    gd.set_golf_pose(4, gt.GolfPose.LhStart, 0.9)

    pose, prob = gd.get_golf_pose(0)
    assert pose == gt.GolfPose.RhStart
    assert prob == 0.7

    pose, prob = gd.get_golf_pose(4)
    assert pose == gt.GolfPose.LhStart
    assert prob == 0.9

def test_frame_poses():
    gd = golf_data.GolfData(10)
    gd.set_golf_pose(0, gt.GolfPose.RhStart, 0.7)
    gd.set_golf_pose(1, gt.GolfPose.LhStart, 0.8)
    gd.set_golf_pose(5, gt.GolfPose.RhStart, 0.9)

    frames = gd.get_pose_frames(gt.GolfPose.RhStart)
    assert len(frames) == 2
    assert frames[0] == 0
    assert frames[1] == 5
 
