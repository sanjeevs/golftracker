#
# Input videos may be too large for our needs.
# Currently restricting them to a max of 500 pixels.
# In open cv 4.6 there is a bug with rotation. https://github.com/opencv/opencv/issues/22088
#

import argparse
from golftracker import video_utils
import cv2
import os
import math


def create_parser():
    """ Create cmd line parser."""
    parser = argparse.ArgumentParser(description="resize, rotate the incoming video")

    parser.add_argument("video", type=str, help="Input video file")

    parser.add_argument(
        "--out", "-o", default="", type=str, help="Output video file name."
    )

    parser.add_argument(
        "--start", default=0, type=int, help="Starting frame idx."
    )

    parser.add_argument(
        "--end", default=-1, type=int, help="Ending frame idx."
    )

    parser.add_argument(
        "--scale", default=100, type=int, help="scale down the video inp pcnt")

    parser.add_argument(
        "--rotate", default=0, type=int, 
        help="rotate the incoming video file. Auto fix for cv2 4.6",
    )

    return parser


def main():
    opt = create_parser().parse_args()

    if opt.out == "":
        fname = os.path.basename(opt.video)
        opt.prefix = os.path.splitext(fname)[0]
        print(opt.prefix)

    cap = cv2.VideoCapture(opt.video)
    if not cap.isOpened():
        raise ValueError(f"Could not open file '{opt.video}'")

   
    print(f">>Scaling the video by {opt.scale}")
    or_meta = int(cap.get(cv2.CAP_PROP_ORIENTATION_META))
    if or_meta == 270:
        print(f">>Found meta={or_meta}:Fixing rotation bug in cv2 4.6. Rotating 180")
        opt.rotate = "180"

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()

    frames, video_spec = video_utils.split_video_to_frames (
        opt.video, opt.scale, opt.rotate)

    out_frames = frames[opt.start : opt.end]
    if opt.out == "":
        opt.out = opt.prefix + "_s_" + str(opt.scale)
        if opt.rotate:
            opt.out += "_r_" + str(opt.rotate)
        opt.out += ".mov"
        print(f">>Generating output video '{opt.out}'' file.")
    else:
        print(f">>Creating output video '{opt.out}'' file.")

    video_utils.join_frames_to_video(opt.out, fps, out_frames)
