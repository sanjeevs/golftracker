'''
List of parameters tuned for canny edge detection.
'''

class CannyEdgeParams:
    def __init__(self):
        # Default arguments
        self.gaussian_blur_kernel = (7,7)
        self.bin_threshold = 125
        self.bin_maxvalue = 255
        self.canny_threshold1 = 100
        self.canny_threshold2 = 200
        self.dilate_kernel = (5, 5)