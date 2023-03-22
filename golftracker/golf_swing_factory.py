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

def create_from_video(video_fname, pose_model):
    (frames, (width, height, fps)) = video_utils.split_video_to_frames(video_fname)
    if len(frames) == 0:
        raise ValueError(f"Found no frames in '{video_fname}'")

    # File size is poor man's check that the file name is correct during reconstitute.
    video_size = os.path.getsize(video_fname)
    return __create(height, width, frames, fps, video_fname, video_size, pose_model)
   

def create_from_image(img_fname, pose_model):
    frame = cv2.imread(img_fname)
    img_size = os.path.getsize(img_fname)
    height, width, _ = frame.shape
    fps = 0
    return __create(height, width, [frame], fps, img_fname, img_size, pose_model)

def __create(height, width, frames, fps, fname, file_size, pose_model):
    gs = golf_swing.GolfSwing(height, width, len(frames), fps, fname, file_size)
    video_landmarks = mp_op.run(frames)
    gs.set_mp_landmarks (video_landmarks)
    # Pass a none value to model to skip pose classification. Used in training the ml model.
    if pose_model is not None:
        gs.set_ml_pose_models(pose_model)
        gs.set_golf_swing_sequence()
      
    return gs