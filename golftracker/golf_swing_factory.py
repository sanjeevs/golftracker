#
# Factory method for creating the root object
#

import copy
import json
import cv2


from golftracker import video_utils
from golftracker import golf_swing
from golftracker import media_pipe_operation as mp_op


def create_from_video(video_fname):
    frames = video_utils.split_video_to_frames(video_fname)
    if len(frames) == 0:
        raise ValueError(f"Found no frames in '{video_fname}'")
    (height, width, _) = frames[0].shape
    gs = golf_swing.GolfSwing(height, width)
    mp_op.run(gs, frames)
    return gs

def create_from_image(image_fname):
    """ For testing it is easier to use just a image. """
    frame = cv2.imread(image_fname)
    (height, width, _) = frame.shape
    gs = golf_swing.GolfSwing(height, width)
    mp_op.run(gs, [frame])
    return gs


def clone(gs):
    """Return a new golf swing that has a deep copy of frame contexts.
    """
    gs_clone = golf_swing.GolfSwing(gs.height, gs.width)
    for idx, landmarks in enumerate(gs.mp_pose_frame_landmarks):
        gs_clone.mp_pose_frame_landmarks[idx] = copy.deepcopy(landmarks)

    return gs_clone


def create_from_json(json_fname):
    with open(json_fname, "r") as fh:
        fmt = json.load(fh)

    in_lst = fmt['frames']
    mp_pose_frame_landmarks = []

    for idx in range(len(in_lst)):
        mp_pose_landmarks = in_lst[idx]["mp_pose_landmarks"]
        mp_pose_frame_landmarks.append(mp_pose_landmarks)

    gs = golf_swing.GolfSwing(fmt['height'], fmt['width'])
    gs.mp_pose_frame_landmarks = mp_pose_frame_landmarks
    return gs
