'''
Tracks the true position of the golf club in the video.
'''

class ClubPosition:
	def __init__(self):
		self.positions = {}

	def set(self, frame_idx, grip_pt, club_head_pt):
		""" A club is a straight line from grip to head. """
		self.positions[frame_idx] = (grip_pt[0], grip_pt[1], 
			                         club_head_pt[0], club_head_pt[1])

	def get(self, frame_idx):
		"""Return the line coordinates as a tuple or None."""
		if frame_idx in self.positions.keys():
			return self.positions[frame_idx]
		else:
			return None