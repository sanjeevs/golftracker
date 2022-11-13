#
# Factory method for creating the root object
#

import copy
import json

from golftracker import video_utils
from golftracker import golf_swing
from golftracker import frame_tracker
from golftracker import media_pipe_operation as mp_op


def create_from_mediapipe(video_fname):
    frames = video_utils.split_video_to_frames(video_fname)
    if len(frames) == 0:
        raise ValueError(f"Found no frames in '{video_fname}'")
    (height, width, _) = frames[0].shape
    gs = golf_swing.GolfSwing(height, width)
    mp_op.run(gs, frames)
    return gs


def clone(gs):
    """Return a new golf swing that has a deep copy of frame contexts.
    """
    gs_clone = golf_swing.GolfSwing(gs.height, gs.width)
    for idx, frame_tracker in enumerate(gs.frame_trackers):
        gs_clone.frame_trackers[idx] = copy.deepcopy(frame_tracker)

    return gs_clone


def create_from_json(json_fname):
    with open(json_fname, "r") as fh:
        fmt = json.load(fh)
    in_lst = fmt['frames']
    frame_trackers = []
    for idx in range(len(in_lst)):
        ft = frame_tracker.FrameTracker(in_lst[idx]["frame_tracker"])
        frame_trackers.append(ft)

    gs = golf_swing.GolfSwing(fmt['height'], fmt['width'])
    gs.frame_trackers = frame_trackers
    return gs
