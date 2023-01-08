#
# Represents the (x, y) coordinate of the pose landmarks.
# This involves scaling the normalized values.
#

from golftracker import gt_const


class Points:
    def __init__(self, row, height, width):
        self.data = {}
        i = 0

        for entry in gt_const.MP_POSE_LANDMARKS:
            self.data[entry] = [int(row[i] * width), int(row[i + 1] * height)]
            i += 4

    def __getitem__(self, key):
        if key not in self.data:
            raise ValueError(f"Invalid key value='{key} in pose landmark lookup")
        return self.data[key]
