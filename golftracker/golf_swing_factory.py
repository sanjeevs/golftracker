#
# Factory method for creating the root object
#

import copy
import json
import cv2


from golftracker import video_utils
from golftracker import golf_swing
from golftracker import golf_data
from golftracker import gt_const
from golftracker import media_pipe_operation as mp_op
from golftracker import ml_pose_operation as ml_op


def create_from_frames(video_fname, frames, pose_model=None):
    if len(frames) == 0:
        raise ValueError(f"Found no frames in '{video_fname}'")
    gs = __create_golf_swing(frames, pose_model)
    gs.set_meta_info(video_fname)
    return gs


def create_from_image(image_fname, pose_model=None):
    """ For testing it is easier to use just a image. """
    frame = cv2.imread(image_fname)
    return __create_golf_swing(image_fname, [frame], pose_model)


def __create_golf_swing(frames, pose_model=None):
    (height, width, _) = frames[0].shape
    gs = golf_swing.GolfSwing(height, width, len(frames))
    mp_op.run(gs, frames)
    if pose_model:
        ml_op.run(gs, pose_model)
        gs.set_pose_sequence()
    return gs