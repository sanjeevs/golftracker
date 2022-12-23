#
# Repository for exporting and importing golf swing
import pickle
import os
from golftracker import file_utils

def serialize(fname, golf_swing):
    with open(fname, "wb") as fh:
        pickle.dump(golf_swing, fh)

def reconstitute(fname, video_dir="."):
    """ Recreate the golfswing. """
    with open(fname, "rb") as fh:
        gs = pickle.load(fh)

    if gs.video_fname:
        f = file_utils.search_file(video_dir, gs.video_fname)
        if f:
            out_size = os.path.getsize(f)
            if out_size == gs.video_size:
                gs.video_fname = f
            else:
                raise ValueError(f">> Video'{f}' byte size is {out_size}. Expected {gs.video_size} bytes")

        else:
            raise ValueError(f">>Could not locate video fname '{gs.video_fname}'' in '{video_dir}'")

    return gs