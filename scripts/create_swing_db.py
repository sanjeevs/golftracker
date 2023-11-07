'''
Process the incoming video and create a database.
'''

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
    parser.add_argument(
        "--truncate", "-t", default=False, action='store_true', help="Truncate the video db"
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
        pose_model = pickle.load(fh)
        print(f">>Loaded default ML model '{opt.model}'")
    
    frames, gs = golf_swing_factory.create_from_video(opt.in_video)
    gs.classify_golf_poses(pose_model)
    gs.find_golf_swing_sequence()
    print(f">>Golf sequence is from {gs.pose_sequence}")
    
    # Dump some useful statistics.
    print(f">>Analyzed {gs.num_frames} frames of golf swing.")

    if gs.is_valid_swing():
        print(f">>Golf swing detected between frame_idx {gs.pose_sequence}")
        print(f">>Golfer is {gs.handed}")    
        golf_swing_repository.serialize(opt.out, gs)

    else:
        print(f">>OOPS could not detect golf swing in the video.")
        print(f">>ERROR: COULD NOT CREATE THE PKL DATABASE!!!")
        print("\n\n")
        print(f">>Run the cmd 'label_golf_poses {opt.in_video}' to create csv file")
        

   
if __name__ == "__main__":
    main()
