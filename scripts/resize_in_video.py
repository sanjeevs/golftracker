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
        "--max_dim",
        "-m",
        default=600,
        type=int,
        help="Max pixel width or height of the video.",
    )

    parser.add_argument(
        "--rotate",
        "-r",
        default="",
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

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if width > opt.max_dim:
        scale_x = opt.max_dim / width
    if height > opt.max_dim:
        scale_y = opt.max_dim / height
    print(f"scale_x={scale_x}, {scale_y}")
    opt.scale = int(min(scale_x, scale_y) * 100)
    opt.scale = math.ceil(opt.scale/10) * 10
    if opt.scale == 0: 
        opt.scale = 100

    print(f">>Orig video has width={width}, ht={height}.")
    print(f">>Scaling the video by {opt.scale}")
    or_meta = int(cap.get(cv2.CAP_PROP_ORIENTATION_META))
    if or_meta == 270:
        print(f">>Found meta={or_meta}:Fixing rotation bug in cv2 4.6. Rotating 180")
        opt.rotate = "180"

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()

    (frames, (w, h, fps)) = video_utils.split_video_to_frames(
        opt.video, opt.scale, opt.rotate
    )
    print(f">>Final video wxh is {w}x{h} at {fps} fps")

    if opt.out == "":
        opt.out = opt.prefix + "_s_" + str(opt.scale)
        if opt.rotate:
            opt.out += "_r_" + opt.rotate
        opt.out += ".mov"
        print(f">>Generating output video '{opt.out}'' file.")
    else:
        print(f">>Creating output video '{opt.out}'' file.")

    video_utils.join_frames_to_video(opt.out, fps, frames)
