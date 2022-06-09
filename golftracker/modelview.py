"""Create frames from the tracker json files."""

import argparse
import json
import os
import os.path
import cv2
import numpy as np

from golftracker import draw
from golftracker import tracker

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Visualize the tracker json files by converting to png."
    )
    parser.add_argument(
        "--suffix",
        "-p",
        default="_model",
        help="Suffix for png file(s). Post append suffix to frame file but with .png suffix.",
    )
    parser.add_argument(
        "jsondir", type=str, help="Filename or dir holding all the json files."
    )
    return parser

def create_frame(json_file, suffix):
    with open(json_file) as json_fh:
        tracker_dict = json.load(json_fh)

    if "frame" not in tracker_dict:
        raise IndexError("Missing frame information in json file")

    w, h = tracker_dict['frame']

    png_fname = os.path.splitext(json_file)[0] + suffix + ".png"
    blank_image = np.zeros((h, w, 3), np.uint8)
    draw.visualize_tracker(blank_image, tracker_dict)
    cv2.imwrite(png_fname, blank_image)


def main():
    """Main program"""
    opt = create_parser().parse_args()

    if os.path.isfile(opt.jsondir):
        create_frame(opt.jsondir, opt.suffix)
    else:
        tracker_files = []

        for f in os.listdir(opt.jsondir):
            split_tup = os.path.splitext(f)

            fname = os.path.join(opt.jsondir, f)
            if os.path.isfile(fname) and split_tup[1] == ".json":
                tracker_files.append(fname)

        print(f">>Found {len(tracker_files)} frames to edit in dir '{opt.jsondir}'")

        for f in tracker_files:
            create_frame(f, opt.suffix)