from golftracker import club_head_params

JSON_DATA = {
  "CannyEdgeParams": {
    "gaussian_blur_kernel": [4, 5],
    "bin_threshold": 125,
    "bin_maxvalue": 255,
    "canny_threshold1": 700,
    "canny_threshold2": 200,
    "dilate_kernel": [5, 5]
  },
  "HoughLineParams": {
    "rho": 1,
    "theta": 0.017453292519943295,
    "threshold": 25,
    "min_line_length": 50,
    "max_line_gap": 20
  },
  "ClubHeadPos": {
    1: [1, 1111],
    2: [102, 152],
    5: [105, 155],
  }
}

def test_json_load():
    p = club_head_params.ClubHeadParams()
    p.load_hints(JSON_DATA)
    assert p.canny_edge_params.gaussian_blur_kernel == (4, 5)
    assert p.canny_edge_params.canny_threshold1 == 700
    assert p.hough_line_params.threshold == 25
    assert p.club_head_points_dict.get(0, None) == None
    assert p.club_head_points_dict[1] == (1, 1111)
    assert p.club_head_points_dict[5] == (105, 155)

