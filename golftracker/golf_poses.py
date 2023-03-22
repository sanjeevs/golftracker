'''
GolfSwingPoses
---------------
Handle all the processing related to golf poses.
'''
from golftracker import gt_const as gt


def get_pose_first_start(poses):
    """ Return the first time the start pose is detected.
        Else return None
    """
    if poses == []:
    	raise ValueError("No poses to detect first pose")

    start_idx = None
    for i, pose in enumerate(poses):
        if pose == gt.GolfPose.RhStart or pose == gt.GolfPose.LhStart:
            start_idx = i
            break
    return start_idx

def get_pose_last_finish(poses):
    """Return the last golf swing finish else return last idx"""
    if len(poses) == 0:
        raise ValueError("Cannot have zero poses")

    finish_idx = None
    for i, pose in enumerate(poses):
        if pose == gt.GolfPose.RhFinish or pose == gt.GolfPose.LhFinish:
            finish_idx = i        
    return finish_idx