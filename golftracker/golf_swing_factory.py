"""
Factory
---------
Create the root instance GolfSwing
"""

import os

from golftracker import video_utils
from golftracker import golf_swing
from golftracker import gt_const
from golftracker import media_pipe_operation as mp_op

import cv2

def create_from_video(video_fname, scale=100, rotate=""):
    (frames, (width, height, fps)) = video_utils.split_video_to_frames(video_fname, 
                                                                       scale=scale, 
                                                                       rotate=rotate)
    if len(frames) == 0:
        raise ValueError(f"Found no frames in '{video_fname}'")

    # File size is poor man's check that the file name is correct during reconstitute.
    video_size = os.path.getsize(video_fname)
    return (frames, __create(height, width, frames, fps, video_fname, video_size))
   

def create_from_image(img_fname):
    """Useful factory routine for pytest. """
    frame = cv2.imread(img_fname)
    img_size = os.path.getsize(img_fname)
    height, width, _ = frame.shape
    fps = 0
    return ([frame], __create(height, width, [frame], fps, img_fname, img_size))

def __create(height, width, frames, fps, fname, file_size):
    gs = golf_swing.GolfSwing(height, width, len(frames), fps, fname, file_size)
    video_landmarks = mp_op.run(frames)
    gs.set_mp_landmarks (video_landmarks)
    return gs