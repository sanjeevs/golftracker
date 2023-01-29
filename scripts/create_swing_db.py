# Dumps out the initial creation of golf swing to json.
# Other scripts can use the db, instead of rerunning mp every time.

import argparse
import os
import pickle

from golftracker import golf_swing_factory
from golftracker import video_utils
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
    
    (frames, _) = video_utils.split_video_to_frames(opt.in_video)
    gs = golf_swing_factory.create_from_frames(opt.in_video, frames, model)

    
    # Dump some useful statistics.
    print(f">>Analyzed {gs.num_frames} frames of golf swing.")
    if gs.pose_sequence != (0, 0):
        print(f">>Golf swing detected from frame_idx {gs.pose_sequence}")
        print(f">>Truncating the frames from {gs.pose_sequence} to '{opt.out}'")
        if gs.is_golfer_right_handed():
            print(f">>Golfer is right handed")
        else:
            print(f">>OOPS Golfer is not right handed")
            print("\n\n")
            print(">>WARNING: Currently only support right handed golfer!!")
        i = gs.pose_sequence[0]
        j = gs.pose_sequence[1] + 1
        swing_frames = frames[i:j]
        trunc_gs = golf_swing_factory.create_from_frames(opt.in_video, swing_frames, model)
        golf_swing_repository.serialize(opt.out, trunc_gs)
    else:
        print(f">>OOPS could not detect golf swing in the video.")
        print("\n\n")
        print(f">>WARNING: NOT CREATING DATABASE AS SWING NOT DETECTED")
        

   
if __name__ == "__main__":
    main()
