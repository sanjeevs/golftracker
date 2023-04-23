from golftracker import hough_line_detector as hl 
from golftracker import hough_line_params
import numpy as np 
import cv2
import os

def test_hough_line_detector():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[50:55, 0:100] = 255
    params = hough_line_params.HoughLineParams()
    params.min_line_length = 1
    params.max_line_gap = 1
    hl_gen = hl.HoughLineDetector(params)
    
    
    # Single channel image and so cannot call run
    lines = hl_gen.process(img)

    assert len(lines) > 1
    assert lines[0][0] == 0
    assert lines[0][1] == 51
    assert lines[0][2] == 99
    assert lines[0][3] == 51