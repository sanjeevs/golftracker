'''
Detect left or right handed golf player.
'''
from golftracker import gt_const as gt

def run(points):
	"""
	Detect if the player is left handed or right handed.
	"""
	return gt.Handedness.RightHanded