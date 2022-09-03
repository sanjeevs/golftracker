"""
 Use mediapipe pose detection on frame(s). All the landmarks detected
 are written into a json file with default name "frame_xx_mp.json"
"""

import argparse
import os
import os.path
import cv2
import json
import mediapipe as mp

mp_pose = mp.solutions.pose

from golftracker import frame_tracker


def create_parser():
    """Create a command line parser."""

    parser = argparse.ArgumentParser(
        description="Run media pipe to detect the pose from all the frames."
    )
    parser.add_argument(
        "--suffix",
        "-s",
        default="_mp",
        help="Suffix for json file(s). Append suffix to base frame file with .json ext.",
    )
    parser.add_argument(
        "framedir", type=str, help="Filename or dir holding all the frame files."
    )
    return parser


def run_mp_pose_on_image(image):
    """ Run google mediapipe pose algo on image and returns trackers.
    :param:frame: incoming frame file.
    :returns:trackers: Frame tracker object
    """

    ft = frame_tracker.FrameTracker()

    # -----------------------------------------------
    # Heart of the logic
    # -----------------------------------------------
    with mp_pose.Pose(
        static_image_mode=True,
        model_complexity=2,
        enable_segmentation=True,
        min_detection_confidence=0.5,
    ) as pose:
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            ft.set_mp_trackers(results.pose_landmarks.landmark)

    return ft


def run_mp_pose(frame_files):
    """ Runs the mediapipe pose on list of frames.
    Returns empty hash if the landmarks were not detected.

    :param:frame_files: A list of frame files.
    :returns:trackers_lst: A list of trackers for each frame.

    """
    trackers_lst = []

    for idx, file in enumerate(frame_files):
        trackers = run_mp_pose_on_image(cv2.imread(file))
        trackers_lst.append(trackers)

    return trackers_lst


def run_mp_pose_to_json(frame_files, suffix="_mp"):
    """ Save the trackers to json files derived from frame files. """

    trackers_lst = run_mp_pose(frame_files)
    json_fnames = tracker_utils.frame_fnames_to_json_fnames(frame_files, opt.suffix)
    print(f">>Created {len(trackers_lst)} trackers for the frames.")
    tracker_utils.trackers_to_json(json_fnames=json_fnames, trackers_lst=trackers_lst)
    return json_fnames


def main():
    """Main program"""
    opt = create_parser().parse_args()

    if os.path.isfile(opt.framedir):
        frame_files = [opt.framedir]
    else:
        frame_files = []

        for f in os.listdir(opt.framedir):
            split_tup = os.path.splitext(f)

            fname = os.path.join(opt.framedir, f)
            if os.path.isfile(fname) and split_tup[1] == ".png":
                frame_files.append(fname)

        print(f">>Found {len(frame_files)} frames to edit in dir '{opt.framedir}'")

    json_fnames = run_mp_pose_to_json(frame_files, op.suffix)
    print(f">>Created {len(json_fnames)} json files from google mediapipe")
