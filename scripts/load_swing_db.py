'''
Load the contents of the json file to pkl data base.
'''
import argparse
import os
import csv
import json

from golftracker import golf_swing_factory
from golftracker import golf_swing_repository
from golftracker import gt_const as gt

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Load info from database")

    parser.add_argument("json", type=str, help="Swing state in json format")
    parser.add_argument("--pkl", type=str, default="", help="input pkl data base to use")
    parser.add_argument("--mp", action="store_true", help="Only update the media pipe")
    parser.add_argument("--club_head", action="store_true", help="Only update club head")
    parser.add_argument("--pose_result", action="store_true", help="Only update pose result")
    parser.add_argument("--all", action="store_true", help="Only update pose result")
    return parser


def main():
    opt = create_parser().parse_args()
    with open(opt.json, 'r') as file:
        data = json.load(file)

    if opt.pkl:
        print(f">>Loading the swing from '{opt.pkl}'")
        gs = golf_swing_repository.reconstitute(opt.pkl)
        out_pkl = opt.pkl
    else:
        print(f">>Creating a new swing from '{opt.json}'")
        gs = golf_swing_factory.create_from_json(data)
        out_pkl = os.path.splitext(os.path.basename(opt.json))[0] + ".pkl"

    if opt.all or opt.mp:
        for idx, row in enumerate(data["mp_result"]):
            landmark = gt.create_pb_normalized_landmarks(row)
            gs.mp_result.video_landmarks[idx] =  landmark

    if opt.all or opt.club_head:
        gs.club_head_result.norm_points = data["club_head_result"]["norm_points"]
        gs.club_head_result.algos = data["club_head_result"]["algos"]

    if opt.all or opt.pose_result:
        for idx, p in enumerate(data["pose_result"]["poses"]):
            gs.pose_result.poses[idx] = gt.GolfPose.__members__.get(p)
        gs.pose_result.handed = gt.Handedness.__members__.get(data["pose_result"]["handed"])

    gs.to_json("out.json", compact=False)
    print(f">>Saving the design to '{out_pkl}'")
    golf_swing_repository.serialize(out_pkl, gs)