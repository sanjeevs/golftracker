'''
Pose model to detect the golf poses.
'''
from golftracker import pose_result
from golftracker import gt_const as gt
import pandas as pd
import numpy as np

class PoseModel:

    def __init__(self, ml_model):
        self.ml_model = ml_model

    def run(self, golf_swing):
        """
        Run the ml model on the flat row of landmarks from media pipe
        to detect golf pose.
        """
        result = pose_result.PoseResult(golf_swing.num_frames)

        for frame_idx in range(golf_swing.num_frames):
            mp_landmarks_flat_row = golf_swing.get_mp_landmarks_flat_row(frame_idx)
            X = pd.DataFrame([mp_landmarks_flat_row])
            pose_class = self.ml_model.predict(X)[0]
            pose_prob = self.ml_model.predict_proba(X) [0]
            max_prob = round(pose_prob[np.argmax(pose_prob)], 2)

            if max_prob > gt.ML_POSE_PROB_THRESHOLD:
                result.poses[frame_idx] = gt.GolfPose[pose_class]
            else:
                result.poses[frame_idx] =  gt.GolfPose.Unknown
        
        start_idx = self.get_first_start_pose_frame_idx(result.poses)
        end_idx = self.get_last_finish_pose_frame_idx(result.poses)
        result.pose_sequence = (start_idx, end_idx)

        if start_idx:
            if result.poses[start_idx] ==  gt.GolfPose.RhStart:
                result.handed = gt.Handedness.RighHanded
            elif pose_result.poses[start_idx] == gt.GolfPose.LhStart:
                result.handed = gt.Handedness.LeftHanded
    
        result.handed == gt.Handedness.Unknown

        return result

    def get_first_start_pose_frame_idx(self, poses):
        """ Return the first time the start pose is detected.
            Else return None
        """
        start_idx = None
        for i, pose in enumerate(poses):
            if pose == gt.GolfPose.RhStart or pose == gt.GolfPose.LhStart:
                start_idx = i
                break
        return start_idx

    def get_last_finish_pose_frame_idx(self, poses):
        """Return the last golf swing finish else return None"""
        finish_idx = None
        for i, pose in enumerate(poses):
            if pose == gt.GolfPose.RhFinish or pose == gt.GolfPose.LhFinish:
                finish_idx = i        
        return finish_idx

    
    