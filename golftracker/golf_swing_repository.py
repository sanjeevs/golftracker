"""
Repository for exporting and importing golf swing.
"""

import pickle
import os
from golftracker import file_utils

def serialize(fname, golf_swing):
    """ Save the golf swing into a pickle data base."""
    # Need to remove the frames if it exists.
    golf_swing.frames = []
    with open(fname, "wb") as fh:
        pickle.dump(golf_swing, fh)

def reconstitute(fname, search_lst=[]):
    """ Recreate the golfswing. """
    with open(fname, "rb") as fh:
        gs = pickle.load(fh)

    # First just search the fname path in pkl.
    # If it does not find it then search the list of directories.
    # Raise exception otherwise
    out_size = -1
    if os.path.exists(gs.video_input.fname):
        out_size = os.path.getsize(gs.video_input.fname)
        video_fname = gs.video_input.fname
    else:
        base_fname = file_utils.basename(gs.video_input.fname)
        for search_d in search_lst:
            f = file_utils.search_file(search_d, base_fname)
            if f:
                out_size = os.path.getsize(f)
                video_fname = os.path.join(search_d, base_fname)
                break

    # Poor man's check that we are pointing to the same vidoe file as before.
    if out_size == -1:
        raise ValueError(f"Could not locate fname '{gs.video_input.fname}. '"
                f"Search path='{search_lst}'")
    elif out_size != gs.video_input.size:
        raise ValueError(f">> Video'{f}' byte size is {out_size}. "
                f"Expected {gs.video_input.size} bytes")
    else:
        gs.video_input = gs.video_input._replace(fname=video_fname)

    return gs