from golftracker import canny_edge_generator as gen 
import numpy as np 
import cv2
import os

def test_null():
    ce_gen = gen.CannyEdgeGenerator(0)
    assert len(ce_gen.param_lst) == 0

def test_blank_frame():
    blank_frame = np.zeros((600, 800, 3), np.uint8)
    ce_gen = gen.CannyEdgeGenerator(1)
    canny_imgs = ce_gen.run([blank_frame])
    assert len(canny_imgs) == 1
    assert id(canny_imgs[0]) != id(blank_frame)

def test_pose1():
    """Test on a single frame that media pipe runs successfully."""
    fname = os.path.join("tests", "assets", "test_pose1.jpg")
    frames = []
    frames.append(cv2.imread(fname))
    ce_gen = gen.CannyEdgeGenerator(1)
    canny_imgs = ce_gen.run(frames)
    assert len(canny_imgs) == 1
    assert canny_imgs[0].shape == frames[0].shape
    #cv2.imshow("canny", canny_imgs[0])
    #cv2.waitKey()