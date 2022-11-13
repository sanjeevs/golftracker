# Script
# Convert a video into a media pipe stick figure video

import argparse
import cv2


from golftracker import video_utils
from golftracker import golf_swing_factory
from golftracker import draw_operation as draw_op


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
        "--fps",
        "-f",
        default=20,
        type=int,
        help="Frames per second of out video"
    )


    return parser

def main():
    opt = create_parser().parse_args()
    gs = golf_swing_factory.create_from_json(opt.json)

    stick_frames = draw_op.run(gs)

    video_utils.join_frames_to_video(opt.out_video, fps=opt.fps, frames=stick_frames)

if __name__ == "__main__":
    main()
