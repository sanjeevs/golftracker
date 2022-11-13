#
# Factory method for creating the root object
#
import video_utils
import golf_swing


def create_from_video(video_fname):
    frames = video_utils.split_video_to_frames(video_fname)
    return golf_swing.GolfSwing(frames)

def clone_new_context(golf_swing):
    """Return a new golf swing that has a deep copy of frame context.
    However the frames are a shallow copy since they are usually read only
    """
    gs = golf_swing.GolfSwing(golf_swing.frames)
    for idx, frame_context in enumerate(golf_swing.frame_contexts):
        gs.frame_contexts[idx] = copy(frame_context)

    return gs