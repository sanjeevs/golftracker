"""
Run hough line detector on images.
"""

from golftracker import hough_line_params as param
import cv2
import numpy as np


class HoughLineDetector:
    def __init__(self, params):
        self.params = params

    def run(self, frames):
        result = []
        for idx, frame in enumerate(frames):
            single_channel_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            lines = self.process(single_channel_img)
            result.append(lines)

        return result

    def process(self, single_channel_img):
        """
        Run hough line detection and return a flat list of points
        """
        lines = cv2.HoughLinesP(
            single_channel_img,
            self.params.rho,
            self.params.theta,
            self.params.threshold,
            np.array([]),
            self.params.min_line_length,
            self.params.max_line_gap,
        )

        # Convert to a flat array of lines.
        result = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                result.append((x1, y1, x2, y2))
        return result
