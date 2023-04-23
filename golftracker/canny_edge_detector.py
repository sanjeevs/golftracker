"""
Generates canny edge images.
"""
from golftracker import canny_edge_params as param
import cv2
import numpy as np


class CannyEdgeDetector:
    def __init__(self, params):
        self.params = params

    def run(self, frames):
        canny_imgs = []
        for idx in range(len(frames)):
            f = self.process(frames[idx])
            canny_imgs.append(cv2.merge((f, f, f)))

        return canny_imgs

    def process(self, img):
        img_blur = cv2.GaussianBlur(img, self.params.gaussian_blur_kernel, 1)
        # this converts it to single channel
        img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
        img_thresh = cv2.threshold(
            img_gray, self.params.bin_threshold, self.params.bin_maxvalue, cv2.THRESH_BINARY_INV
        )[1]
        img_canny = cv2.Canny(
            img_thresh, self.params.canny_threshold1, self.params.canny_threshold2
        )
        kernel = np.ones(self.params.dilate_kernel)
        img_dil = cv2.dilate(img_canny, kernel, iterations=1)
        # Convert single channel to 3 channel
        return img_dil