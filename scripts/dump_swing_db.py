"""
Dump all the relevant information from a swing database.
"""
import argparse
import os


from golftracker import golf_swing_factory
from golftracker import golf_swing_repository
from golftracker import gt_const as gt

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Dump info from database")

    parser.add_argument("pkl_db", type=str, help="Swing database in pkl format")

    return parser


def main():
    opt = create_parser().parse_args()

    gs = golf_swing_repository.reconstitute(opt.pkl_db)

    print(f">>Loading pickle database {opt.pkl_db}")
    print(
        f">>Found {gs.num_frames} frames of w={gs.width}, h={gs.height} at {gs.fps} fps"
    )
    print(f">>Video file is {gs.video_fname} of {gs.video_size} bytes")

    print("\n\n>>Dumping golf poses")
   
    if gs.is_golfer_right_handed():
        print(">>Golfer is right handed")

    print(f">>Golf pose sequence is from {gs.pose_sequence}")