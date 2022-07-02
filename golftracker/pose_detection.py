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

from golftracker import mp_tracker


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
    :returns:trackers: Hash of all the trackers
    """

    trackers = {}

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
            mp_tracker.add_mp_landmarks(
                trackers, results.pose_landmarks.landmark
            )

    return trackers


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


def trackers_to_json_str(trackers):
    """Return a json str for the trackers."""

    return json.dumps(trackers)


def trackers_to_json(json_fnames, trackers_lst):
    """Write the trackers to json files."""

    for idx, f in enumerate(json_fnames):
        with open(f, "w") as fh:
            fh.write(trackers_to_json_str(trackers_lst[idx]))


def frame_fnames_to_json_fnames(frame_fnames, suffix):
    """Return the list of json fnames from frame fnames."""

    json_fnames = []
    for idx, f in enumerate(frame_fnames):
        split_tup = os.path.splitext(f)
        json_fnames.append(split_tup[0] + suffix + ".json")

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

    json_files = frame_fnames_to_json_fnames(frame_files)

    trackers_lst = run_mp_pose(frame_files)
    print(f">>Created {len(trackers_lst)} trackers for the frames.")

    trackers_to_json(trackers_lst, json_files)
