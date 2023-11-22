'''
Process the incoming video and create a database.
'''

import argparse
import os
import pickle

from golftracker import golf_swing_factory
from golftracker import video_utils
from golftracker import golf_swing_repository
from golftracker import pose_model
from golftracker import club_head_params
from golftracker import club_head_detector

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
    parser.add_argument(
        "--scale", "-s", default=100, type=int, 
            help="resize the incoming video file by scale percent",
    )

    parser.add_argument(
        "--rotate", "-r", default="", help="rotate the incoming video file",
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
        ml_model = pickle.load(fh)
        print(f">>Loaded default ML model '{opt.model}'")
    
    video_input = video_utils.VideoInput(fname=opt.in_video, 
            size=os.path.getsize(opt.in_video))
    frames, video_spec = video_utils.split_video_to_frames(opt.in_video,
            scale=opt.scale, rotate=opt.rotate)

    pmodel = pose_model.PoseModel(ml_model)
    ch_params = club_head_params.ClubHeadParams()
    ch_model = club_head_detector.ClubHeadDetector(ch_params)

    gs = golf_swing_factory.create_from_video(video_input, video_spec, frames, 
            pmodel, ch_model)
    print(f">>Golf sequence is from {gs.pose_result.sequence}")
    
    # Dump some useful statistics.
    print(f">>Analyzed {gs.video_spec.num_frames} frames of golf swing.")

    if gs.pose_result.is_valid_swing():
        print(f">>Golf swing detected between frame_idx {gs.pose_result.sequence}")
        print(f">>Golfer is {gs.pose_result.handed}")    
        
    else:
        print(f">>OOPS could not detect golf swing in the video.")
        print(f">>Run'label_golf_poses {opt.out}' to create data for pose model")

    print(f">>Creating the pkl database '{opt.out}'")
    golf_swing_repository.serialize(opt.out, gs)

   
if __name__ == "__main__":
    main()
