#
# Factory method for creating the root object
#
import video_utils
import golf_swing
import copy

def create_from_video(video_fname):
    frames = video_utils.split_video_to_frames(video_fname)
    return golf_swing.GolfSwing(frames)

def clone_new_context(gs):
    """Return a new golf swing that has a deep copy of frame context.
    However the frames are a shallow copy since they are usually read only
    """
    gs_clone = golf_swing.GolfSwing(gs.frames)
    for idx, frame_context in enumerate(gs.frame_contexts):
        gs_clone.frame_contexts[idx] = copy.deepcopy(frame_context)

    return gs_clone