'''
Detect club head in a video.
'''
from golftracker import golf_swing
from golftracker import image_utils
from golftracker import club_head_params


class ClubHeadDetector:
    def __init__(self, golf_swing, params):
        self.gs = golf_swing
        self.params = params
        self.club_head_screen_points = [None] * self.gs.num_frames

    def run(self):
        # Copy over the labels created by the user.
        for k, v in self.params.club_head_norm_points_dict.items():
            screen_pt = image_utils.scale_norm_point(k, self.gs.width,
                    self.gs.height)
            self.club_head_screen_points[k] = screen_pt

    def screen_point(self, frame_idx):
        return self.club_head_screen_points[frame_idx]
