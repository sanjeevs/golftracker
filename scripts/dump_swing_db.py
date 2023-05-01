"""
Dump all the relevant information from a swing database.
"""
import argparse
import os
import csv

from golftracker import golf_swing_factory
from golftracker import golf_swing_repository
from golftracker import gt_const as gt

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Dump info from database")

    parser.add_argument("pkl_db", type=str, help="Swing database in pkl format")
    parser.add_argument("--csv", type=str, help="csv file to dump the points", default="")
    return parser


def main():
    opt = create_parser().parse_args()

    gs = golf_swing_repository.reconstitute(opt.pkl_db)

    print(f">>Loading pickle database {opt.pkl_db}")
    print(
        f">>Found {gs.num_frames} frames of w={gs.width}, h={gs.height} at {gs.fps} fps"
    )
    print(f">>Video file is {gs.video_fname} of size {gs.video_size} bytes")

    if opt.csv == "":
        opt.csv = os.path.splitext(opt.pkl_db)[0] + ".csv"

    print(f">>Saving point values in '{opt.csv}'' file")
    with open(opt.csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(gt.MP_POSE_LANDMARKS)

        for frame_idx in range(gs.num_frames):
            points = gs.get_norm_mp_points(frame_idx)  
            row = [coord for pair in points.values() for coord in pair]
            writer.writerow(row)