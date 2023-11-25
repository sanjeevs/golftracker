"""
Factory
---------
Create the root instance GolfSwing
"""

import os

from golftracker import image_utils, video_utils
from golftracker import golf_swing
from golftracker import gt_const
from golftracker import media_pipe_operation as mp_op

import cv2
import json

def create_from_video(video_input, video_spec, frames, pose_model=None,
        club_head_detector=None):
    return __create(video_spec, video_input, frames, pose_model,
                club_head_detector)
   
def create_from_image(img_fname, frame):
    """Useful factory routine for pytest. """
    img_size = os.path.getsize(img_fname)
    height, width, _ = frame.shape
    video_spec = video_utils.VideoSpec(height=height, width=width, fps=0,
            scale=100, rotate=0, num_frames=1)
    video_input = video_utils.VideoInput(fname=img_fname, size=img_size)
    return __create(video_spec, video_input, [frame], None, None)


def __create(video_spec, video_input, frames, pose_model, club_head_detector):
    gs = golf_swing.GolfSwing(video_spec, video_input)
    gs.frames = frames

    # Run media pipe first
    video_landmarks = mp_op.run(frames)
    gs.set_mp_landmarks(video_landmarks)

    if pose_model:
        # Detect the start and end pose of the golf swing
        pose_result = pose_model.run(gs)
        gs.pose_result = pose_result

    if club_head_detector:
        # Estimate the club head position.
        club_head_result = club_head_detector.run(gs)
        gs.club_head_result.reset_and_update(club_head_result)

    return gs

def create_from_json(data):
    
    video_spec_data = data["video_spec"]
    video_input_data = data["video_input"]

    video_spec = video_utils.VideoSpec(**video_spec_data)
    video_input = video_utils.VideoInput(**video_input_data)
    return golf_swing.GolfSwing(video_spec, video_input)
