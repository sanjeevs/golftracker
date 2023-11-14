'''
Detect club head in a video.
'''
from golftracker import golf_swing
from golftracker import club_head_result
from golftracker import image_utils

class ClubHeadDetector:
    def __init__(self, club_head_params):
        self.params = club_head_params

    def run(self, golf_swing):
        ch_result = club_head_result.ClubHeadResult(golf_swing.num_frames)
       
        height, width = golf_swing.height, golf_swing.width

        # Copy over the labels created by the user.
        for k, v in self.params.club_head_norm_points_dict.items():
            screen_pt = image_utils.scale_norm_point(k, width, height)
            ch_result.points[k] = screen_pt

        return ch_result

   