from golftracker import ml_pose_operation
from unittest.mock import Mock
from golftracker import gt_const as gt


def test_null():
	ml_model = Mock()

	pose = ml_pose_operation.run(ml_model, [], 0.8)
	assert pose == gt.GolfPose.Unknown

def test_unknown():
	ml_model = Mock()
	ml_model.predict.return_value = ['RhStart']
	ml_model.predict_proba.return_value = [[0.1, 0.2, 0.7]]

	pose = ml_pose_operation.run(ml_model, [], 0.8)
	assert pose == gt.GolfPose.Unknown