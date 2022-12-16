#
# Represents the (x, y) coordinate of the pose landmarks.
# This involves scaling the normalized values.
#

from golftracker import gt_const

class Points:

    def __init__(self, landmarks, height, width):
        self.data = {}
        i = 0

        for entry in gt_const.MP_POSE_LANDMARKS:
            if landmarks:
                self.data[entry] = [landmarks[i] * width, landmarks[i + 1] * height]
                i += 4
            else:
                self.data[entry] = []


    def __getitem__(self, key):
        if key not in self.data:
            raise ValueError(f"Invalid key value='{key} in pose landmark lookup")
        return self.data[key]
