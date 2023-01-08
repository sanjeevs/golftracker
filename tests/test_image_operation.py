from golftracker import image_operation
import numpy as np


def test_blank():
    h = w = 100
    frame = np.zeros((h, w, 3), np.uint8)
    canny = image_operation.CannyEdgeDetection()
    f = canny.process(frame)
    assert f.shape == frame.shape
    lst = canny.run([frame])
    assert len(lst) == 1
    assert lst[0].shape == frame.shape