from golftracker import pose_model
from unittest.mock import Mock
from golftracker import gt_const as gt


def test_unknown():
    ml_model = Mock()
    ml_model.predict.return_value = ['RhStart']
    ml_model.predict_proba.return_value = [[0.1, 0.2, 0.7]]
    golf_swing = Mock()
    golf_swing.num_frames = 1
    golf_swing.get_mp_landmarks_flat_row.return_value = [[0, 0, 0, 0]]

    pm = pose_model.PoseModel(ml_model)
    result = pm.run(golf_swing)
    assert result.poses[0] == gt.GolfPose.Unknown