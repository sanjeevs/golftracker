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

    def __str__(self):
        return f"BinThreshold={self.bin_threshold}, " \
               f"BinMax={self.bin_maxvalue}, "\
               f"Thresh1={self.canny_threshold1}, " \
               f"Thresh2={self.canny_threshold2}"

    def load_from_json(self, params):
      lst = tuple(params.get('gaussian_blur_kernel', self.gaussian_blur_kernel))
      self.gaussian_blur_kernel = (int(lst[0]), int(lst[1]))
      self.bin_threshold = int(params.get('bin_threshold', self.bin_threshold))
      self.bin_maxvalue = int(params.get('bin_maxvalue', self.bin_maxvalue))
      self.canny_threshold1 = int(params.get('canny_threshold1', self.canny_threshold1))
      self.canny_threshold2 = int(params.get('canny_threshold2', self.canny_threshold2))
      lst = tuple(params.get('dilate_kernel', self.dilate_kernel))
      self.dilate_kernel = (int(lst[0]), int(lst[1]))