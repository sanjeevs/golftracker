#
# Runs ml model to detect the poses
import pandas as pd
import numpy as np 
from golftracker import gt_const as gt


def run(golf_swing, model):

    for idx in range(golf_swing.num_frames):
        X = pd.DataFrame([golf_swing.get_mp_landmarks_flat_row(idx)])

        pose_class = model.predict(X)[0]
        pose_prob = model.predict_proba(X)[0]
        max_prob = round(pose_prob[np.argmax(pose_prob)], 2)

        if max_prob > 0.70:
            golf_swing.set_golf_pose(idx, gt.GolfPose[pose_class], max_prob)
