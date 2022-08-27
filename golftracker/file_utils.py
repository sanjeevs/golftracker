""" File utils for creating, deleting files dirs """
import os
import shutil
import re

def create_framedir(dirname, empty=1):
    """Create a clean frame dir."""
    if os.path.exists(dirname):
        if empty:
            shutil.rmtree(dirname)
        else:
            raise ValueError(f"Dir '$dirname' already exists")
    os.mkdir(dirname)
    if os.path.exists(dirname):
        print(f">>Created '{dirname}' for storing frames")

def select_frame_fnames_from_dir(framedir, match_exp):
    """
    Select matching file names from a directory.

    >>> select_frame_fnames_from_dir(".", "file_utils")
    []


    """
    fnames = [f for f in os.listdir(framedir) if os.path.isfile(os.path.join(framedir, f)) and
              os.path.splitext(f)[1] == ".png"]
    matching_fnames = []
    for f in fnames:
        m = re.match(match_exp, f)
        if m:
            matching_fnames.append(os.path.join(framedir, f))
    matching_fnames.sort()
    return matching_fnames

def create_frame_fnames(num_frames, prefix="frame_"):
    """
    Create the list of frame file names based on the number of frames.
    The number of digits is the same in all the fnames for easy sorting.

    >>> create_frame_fnames(3)
    ['frame_0.png', 'frame_1.png', 'frame_2.png']

    >>> create_frame_fnames(100)[0]
    'frame_00.png'

    >>> create_frame_fnames(100)[-1]
    'frame_99.png'

    >>> create_frame_fnames(101)[-1]
    'frame_100.png'

    """
    if num_frames == 0:
        raise ValueError("Number of frames needs to be > 0")
    elif num_frames < 10:
        num_digits = 1
    else:
        num_digits = len(str(num_frames -1))

    frame_fnames = []
    for idx in range(num_frames):
        fname = prefix + str(idx).zfill(num_digits) + ".png"
        frame_fnames.append(fname)
    return frame_fnames

def frame_fnames_to_json_fnames(frame_fnames, suffix):
    """
    Return the list of json fnames from frame fnames.

    >>> frame_fnames_to_json_fnames(["frame_000.png"], "_mp")
    ['frame_000_mp.json']


    >>> frame_fnames_to_json_fnames(["outdir/frame_0.png"], "_mp")
    ['outdir/frame_0_mp.json']

    """

    json_fnames = []
    for idx, f in enumerate(frame_fnames):
        split_tup = os.path.splitext(f)
        json_fnames.append(split_tup[0] + suffix + ".json")

    return json_fnames

def json_fnames_to_frame_fnames(json_fnames, prefix=""):
    """
    Return the list of frame fnames from json fnames.

    >>> json_fnames_to_frame_fnames(['frame_00_mp.json'])
    ['frame_00_mp.png']


    >>> json_fnames_to_frame_fnames(['frame_00_mp.json'], prefix="out")
    ['out_00_mp.png']

    >>> json_fnames_to_frame_fnames(['frame_00_mp_final.json'], prefix="out")
    ['out_00_mp_final.png']
    """
    frame_fnames = []
    for idx, f in enumerate(json_fnames):
        if prefix == "":
            split_tup = os.path.splitext(f)
            frame_fnames.append(split_tup[0] + ".png")
        else:
            m = re.search(".*_([\d]+)_(.*).json", f)
            if m:
                fname = prefix + "_" + m.group(1) + "_" + m.group(2) + ".png"
                frame_fnames.append(fname)
            else:
                raise ValueError(f"Could not parse json file '{f}' corrrectly")
    return frame_fnames
