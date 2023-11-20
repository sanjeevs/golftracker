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
       
        height = golf_swing.video_spec.height
        width = golf_swing.video_spec.width

        # Copy over the labels created by the user.
        for k, v in self.params.club_head_points_dict.items():
            ch_result.points[k] = v
            ch_result.algos[k] = 'Label'

        return ch_result
