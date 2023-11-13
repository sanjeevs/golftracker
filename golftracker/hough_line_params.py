'''
List of parameters for Hough Line Detection.
'''
import numpy as np

class HoughLineParams:
    def __init__(self):
        self.rho = 1  # distance resolution in pixels of the Hough grid
        self.theta = np.pi / 180  # angular resolution in radians of the Hough grid
        self.threshold = 15  # minimum number of votes (intersections in Hough grid cell)
        self.min_line_length = 50  # minimum number of pixels making up a line
        self.max_line_gap = 20  # maximum gap in pixels between connectable line segments

    def __str__(self):
        return f"rho={self.rho}, theta={self.theta}, threshold={self.threshold}, " \
               f"min_line_length={self.min_line_length}, " \
               f"max_line_gap={self.max_line_gap}"

    def load_from_json(self, params):
        self.rho = params.get('rho', self.rho)
        self.theta = params.get('theta', self.theta)
        self.threshold = params.get('threshold', self.threshold)
        self.min_line_length = params.get('min_line_length', self.min_line_length)
        self.max_line_gap = params.get('max_line_gap', self.max_line_gap)