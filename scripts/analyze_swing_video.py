# Dumps out the initial creation of golf swing to json.
# Other scripts can use the db, instead of rerunning mp every time.

import argparse
import os
import pickle

from golftracker import golf_swing_factory
from golftracker import golf_swing_repository

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Analyze the golf swing video")

    parser.add_argument("in_video", type=str, help="Input video file name")

    parser.add_argument(
        "--model", "-m", default="", type=str, help="ML model used"
    )
    parser.add_argument(
        "--out", "-o", default="", type=str, help="Output swing pkl database produced"
    )

    return parser


def main():
    opt = create_parser().parse_args()
    if opt.out == "":
        base = os.path.basename(opt.in_video)
        fname = os.path.splitext(base)[0]
        opt.out = fname + ".pkl"

    print(f">>Process '{opt.in_video}' to create '{opt.out}' fname")

    if opt.model == "":
        opt.model = os.path.join("..", "models", "pose_model.pkl")

    with open(opt.model, "rb") as fh:
        model = pickle.load(fh)
        print(f">>Loaded default ML model '{opt.model}'")
    
    
    gs = golf_swing_factory.create_from_video(opt.in_video, model)

    golf_swing_repository.serialize(opt.out, gs)
   
    # Dump some useful statistics.
    print(f">>Analyzed {gs.num_frames} frames of golf swing.")
    poses = gs.get_poses_in_frames()
    for k, v in poses.items():
        print(f"{k}=>{v}")

if __name__ == "__main__":
    main()
