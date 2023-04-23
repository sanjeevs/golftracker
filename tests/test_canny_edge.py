from golftracker import canny_edge_detector as ce
from golftracker import canny_edge_params
import numpy as np 
import cv2
import os


def test_blank_frame():
    blank_frame = np.zeros((600, 800, 3), np.uint8)
    params = canny_edge_params.CannyEdgeParams()
    ce_det = ce.CannyEdgeDetector(params)
    canny_imgs = ce_det.run([blank_frame])
    assert len(canny_imgs) == 1
    assert id(canny_imgs[0]) != id(blank_frame)

def test_pose1():
    """Test on a single frame that media pipe runs successfully."""
    fname = os.path.join("tests", "assets", "test_pose1.jpg")
    frames = []
    frames.append(cv2.imread(fname))
    params = canny_edge_params.CannyEdgeParams()
    ce_det = ce.CannyEdgeDetector(params)
    canny_imgs = ce_det.run(frames)
    assert len(canny_imgs) == 1
    assert canny_imgs[0].shape == frames[0].shape
    #cv2.imshow("canny", canny_imgs[0])
    #cv2.waitKey()