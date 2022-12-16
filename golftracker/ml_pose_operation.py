#
# Runs ml model to detect the poses
import pandas as pd
import numpy as np 

def run(golf_swing, model):

    for idx in range(golf_swing.num_frames):
        X = pd.DataFrame([golf_swing.mp_landmarks_flat_row(idx)])

        pose_class = model.predict(X)[0]
        pose_prob = model.predict_proba(X)[0]
        max_prob = round(pose_prob[np.argmax(pose_prob)], 2)

        if max_prob > 0.50:
            golf_swing.set_ml_pose(idx, pose_class, max_prob)
