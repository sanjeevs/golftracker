"""
Run Machine Learning Model
----------------------------

Runs ml model on the media pipe landmarks to detect the various golf poses.
"""

import pandas as pd
import numpy as np 
from golftracker import gt_const as gt


def run(ml_model, mp_landmarks_flat_row, prob_thresh):
    """
    Run the ml model on the flat row of landmarks from media pipe
    to detect golf pose.

    :param ml_model: machine learning model to use
    :param frame_landmarks: A list holding the proto buffer of each mp landmark.
    :return: GolfPose detected with probability greater than prob_thresh
    :rtype: gt.GolfPose
    """
    if mp_landmarks_flat_row == []:
        return gt.GolfPose.Unknown

    X = pd.DataFrame([mp_landmarks_flat_row])
    pose_class = ml_model.predict(X)[0]
    pose_prob = ml_model.predict_proba(X) [0]
    max_prob = round(pose_prob[np.argmax(pose_prob)], 2)

    if max_prob > prob_thresh:
        return gt.GolfPose[pose_class]
    else:
        return gt.GolfPose.Unknown