# Dumps out the initial creation of golf swing to json.
# Other scripts can use the db, instead of rerunning mp every time.

import argparse
import os
from golftracker import golf_swing_factory


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Save the golfswing to json file")

    parser.add_argument("in_video", type=str, help="Input video file name")

    parser.add_argument(
        "--out", "-o", default="", type=str, help="Output json file produced"
    )

    return parser


def main():
    opt = create_parser().parse_args()
    if opt.out == "":
        base = os.path.basename(opt.in_video)
        fname = os.path.splitext(base)[0]
        opt.out = fname + ".json"

    print(f">>Process '{opt.in_video}' to create '{opt.out}' fname")

    gs = golf_swing_factory.create_from_mediapipe(opt.in_video)

    gs.save_to_json(opt.out)


if __name__ == "__main__":
    main()
