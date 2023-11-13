'''
Input parameters.
'''
from golftracker import canny_edge_params
from golftracker import hough_line_params

class ClubHeadParams:
    def __init__(self):
        self.club_head_norm_points_dict = {}
        self.canny_edge_params = canny_edge_params.CannyEdgeParams()
        self.hough_line_params = hough_line_params.HoughLineParams()


    def load_hints(self, json_data):
        ce_dict = json_data.get("CannyEdgeParams", {})
        self.canny_edge_params.load_from_json(ce_dict)

        hg_dict = json_data.get("HoughLineParams", {})
        self.hough_line_params.load_from_json(hg_dict)

        ch_dict = json_data.get("ClubHeadPos", {})
        for k, v in ch_dict.items(): 
            self.club_head_norm_points_dict[int(k)] = tuple(v)


