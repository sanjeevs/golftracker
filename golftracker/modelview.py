"""Create frames from the tracker json files."""

import argparse
import json
import os
import os.path
import cv2
import numpy as np

from golftracker import draw
from golftracker import tracker_utils


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Visualize the tracker json files by converting to png."
    )
    parser.add_argument(
        "--suffix",
        "-p",
        default="_out",
        help="Suffix for png file(s). Post append suffix to frame file but with .png suffix.",
    )
    parser.add_argument(
        "jsondir", type=str, help="Filename or dir holding all the json files."
    )
    return parser


def create_tracker_frame(png_fname, json_file, width, height):
    """ Convert a json file to png file. """

    with open(json_file) as json_fh:
        trackers = json.load(json_fh)

    blank_image = np.zeros((height, width, 3), np.uint8)

    draw.visualize_trackers(blank_image, trackers)
    print(f"Creating {png_fname}")
    cv2.imwrite(png_fname, blank_image)

def create_tracker_frames(json_fnames, width, height, suffix):
    frame_fnames = tracker_utils.json_fnames_to_frame_fnames(json_fnames, suffix)
    print(frame_fnames)
    for idx, out_fname in enumerate(frame_fnames):
        create_tracker_frame(frame_fnames[idx], json_fnames[idx], width, height)

def main():
    """Main program"""

    opt = create_parser().parse_args()

    if os.path.isfile(opt.jsondir):
        create_tracker_frame(opt.jsondir, opt.suffix)
    else:
        tracker_files = []

        for f in os.listdir(opt.jsondir):
            split_tup = os.path.splitext(f)

            fname = os.path.join(opt.jsondir, f)
            if os.path.isfile(fname) and split_tup[1] == ".json":
                tracker_files.append(fname)

        print(f">>Found {len(tracker_files)} frames to edit in dir '{opt.jsondir}'")

        for f in tracker_files:
            create_tracker_frame(f, opt.suffix)