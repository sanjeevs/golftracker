#
# Factory method for creating the root object
#

import copy
import json
import cv2


from golftracker import video_utils
from golftracker import golf_swing
from golftracker import media_pipe_operation as mp_op
from golftracker import ml_pose_operation as ml_op


def create_from_video(video_fname, pose_model):
    frames = video_utils.split_video_to_frames(video_fname)
    if len(frames) == 0:
        raise ValueError(f"Found no frames in '{video_fname}'")
    return __create_golf_swing(frames, pose_model)


def create_from_image(image_fname, pose_model):
    """ For testing it is easier to use just a image. """
    frame = cv2.imread(image_fname)
    return __create_golf_swing([frame], pose_model)


def __create_golf_swing(frames, pose_model):
    (height, width, _) = frames[0].shape
    gs = golf_swing.GolfSwing(height, width, len(frames))
    mp_op.run(gs, frames)
    if pose_model:
        ml_op.run(gs, pose_model)
    return gs


def create_from_json(json_str):
    json_dict = json.loads(json_str)
    h = json_dict["height"]
    w = json_dict["width"]
    n = json_dict["num_frames"]
    gs = golf_swing.GolfSwing(height=h, width=w, num_frames=n)
    gs.data = json_dict["data"]
    return gs
