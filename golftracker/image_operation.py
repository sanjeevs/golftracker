'''
Wrapper around cv2 algorithm.
Keep it generic.
'''

import cv2
import numpy as np
import logging


class CannyEdgeDetection:
    def __init__(self):
        self.gaussian_blur_kernel = (7,7)
        self.bin_threshold = 125
        self.bin_maxvalue = 255
        self.canny_threshold1 = 100
        self.canny_threshold2 = 200
        self.dilate_kernel = (5, 5)

    def process(self, img):
        img_blur = cv2.GaussianBlur(img, self.gaussian_blur_kernel , 1)
        # this converts it to single channel
        img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
        img_thresh = cv2.threshold(img_gray, self.bin_threshold, self.bin_maxvalue, cv2.THRESH_BINARY_INV)[1]
        img_canny = cv2.Canny(img_thresh, self.canny_threshold1, self.canny_threshold2)
        kernel = np.ones(self.dilate_kernel)
        img_dil = cv2.dilate(img_canny, kernel, iterations=1)
        # Convert single channel to 3 channel
        return cv2.merge((img_dil, img_dil, img_dil))

    def run(self, frames):
        return list(map(self.process, frames))

class HoughLineDetector:
    def __init__(self):
        self.rho = 1  # distance resolution in pixels of the Hough grid
        self.theta = np.pi / 180  # angular resolution in radians of the Hough grid
        self.threshold = 15  # minimum number of votes (intersections in Hough grid cell)
        self.min_line_length = 50  # minimum number of pixels making up a line
        self.max_line_gap = 20  # maximum gap in pixels between connectable line segments

    def process(self, canny_edges_img):
        # Run Hough on edge detected image
        # Output "lines" is an array containing endpoints of detected line segments
        lines = cv2.HoughLinesP(canny_edges_img, self.rho, self.theta, self.threshold, np.array([]),
                    self.min_line_length, self.max_line_gap)

        # Convert to a flat array of lines.
        result = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                result.append((x1, y1, x2, y2))
        return result

    def run(self, frames):
        return list(map(self.process, frames))

    def draw(self, canny_edges_img, background_img=None):
        lines = self.process(canny_edges_img)
        if not background_img:
            background_img = np.copy(canny_edges_img) * 0

        for x1, y1, x2, y2 in lines:
            cv2.line(background_img,(x1,y1), (x2,y2), (255,0,0), 5)
        return background_img