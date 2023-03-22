'''
Detect left or right handed golf player.
'''
from golftracker import gt_const as gt

def run(mp_points):
	"""
	Detect if the player is left handed or right handed.
	"""
	return gt.Handedness.RightHanded