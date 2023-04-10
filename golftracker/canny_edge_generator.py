"""
Generates canny edge images.
"""
from golftracker import canny_edge_params as param
import cv2
import numpy as np


class CannyEdgeGenerator:
    def __init__(self, nframes):
        self.param_lst = [param.CannyEdgeParams()] * nframes

    def run(self, frames):
        canny_imgs = []
        for idx in range(len(frames)):
            canny_imgs.append(self.process(frames[idx], self.param_lst[idx]))

        return canny_imgs

    def process(self, img, params):
        """
        Run canny edge algorithm on a frame.
        Return a 3 channel image.
        """
        img_blur = cv2.GaussianBlur(img, params.gaussian_blur_kernel, 1)
        # this converts it to single channel
        img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
        img_thresh = cv2.threshold(
            img_gray, params.bin_threshold, params.bin_maxvalue, cv2.THRESH_BINARY_INV
        )[1]
        img_canny = cv2.Canny(
            img_thresh, params.canny_threshold1, params.canny_threshold2
        )
        kernel = np.ones(params.dilate_kernel)
        img_dil = cv2.dilate(img_canny, kernel, iterations=1)
        # Convert single channel to 3 channel
        return cv2.merge((img_dil, img_dil, img_dil))
