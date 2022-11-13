# Script
# Convert a video into a media pipe stick figure video

import argparse
import cv2


from golftracker import video_utils
from golftracker import golf_swing as gs
from golftracker import draw_operation as draw_op
from golftracker import media_pipe_operation as mp_op


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Create a video of the json golf swing"
    )

    parser.add_argument(
        "json", type=str, help="Input golf swing json database"
    )

    parser.add_argument(
        "out_video", type=str, help="Ouput video file name"
    )

    parser.add_argument(
        "--scale",
        "-s",
        default=100,
        type=int,
        help="resize the incoming video file by scale percent"
    )

    parser.add_argument(
        "--fps",
        "-f",
        default=20,
        type=int,
        help="Frames per second of out video"
    )

    parser.add_argument(
        "--rotate",
        "-r",
        default="",
        help="rotate the incoming video file",
    )

    return parser

def transform_frame(opt, frame):
    if opt.rotate == "90":
        out_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif opt.rotate == "180":
        out_frame = cv2.rotate(frame, cv2.ROTATE_180)
    else:
        out_frame = frame

    return out_frame


def main():
    opt = create_parser().parse_args()
    gs = golf_swing_factory.create_from_json(opt.json)

    stick_frames = draw_op.run(golf_swing)

    video_utils.join_frames_to_fname(opt.out_video, fps=opt.fps, frames=stick_frames)

if __name__ == "__main__":
    main()
