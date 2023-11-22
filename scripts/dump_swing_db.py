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
    return parser


def main():
    opt = create_parser().parse_args()

    gs = golf_swing_repository.reconstitute(opt.pkl_db)
    width, height, fps = gs.video_spec.width, gs.video_spec.height, gs.video_spec.fps

    print(f">>Loading pickle database {opt.pkl_db}")
    print(
        f">>VideoSpec: NumFrames={gs.num_frames} Width={width}, Height={height}, Fps={fps}"
    )
    print(
        f">>VideoFile: Fname={gs.video_input.fname}, Size={gs.video_input.size} bytes"
    )

    print(
        f">>PoseResult: {gs.pose_result}"
    )

    print("\n")
    print(f">>Poses:{gs.pose_result.poses}")
    print("\n")
    
    print(
        f">>ClubHead: {gs.club_head_result}"
    )
    
