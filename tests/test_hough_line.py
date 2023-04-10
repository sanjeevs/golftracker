from golftracker import hough_line_generator as gen 
import numpy as np 
import cv2
import os

def test_null():
    hl_gen = gen.HoughLineGenerator(0)
    assert len(hl_gen.param_lst) == 0

def test_hough_line_detector():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[50:55, 0:100] = 255
    hl_gen = gen.HoughLineGenerator(1)
    hl_gen.param_lst[0].min_line_length = 1
    hl_gen.param_lst[0].max_line_gap = 1
    
    # Single channel image and so cannot call run
    lines = hl_gen.process(img, hl_gen.param_lst[0])

    assert len(lines) > 1
    assert lines[0][0] == 0
    assert lines[0][1] == 51
    assert lines[0][2] == 99
    assert lines[0][3] == 51