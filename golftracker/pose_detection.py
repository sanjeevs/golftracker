""" Use mediapipe pose detection on all the frames."""


import argparse
import os
import os.path
import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose


from golftracker import tracker
from golftracker import draw


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Run media pipe to detect the pose from all the frames."
    )
    parser.add_argument(
        "--prefix",
        "-p",
        default="",
        help="Prefix for json file(s). Append prefix to frame file but with .json suffix.",
    )
    parser.add_argument(
        "framedir", type=str, help="Filename or dir holding all the frame files."
    )
    return parser


def main():
    """Main program"""
    opt = create_parser().parse_args()

    if os.path.isfile(opt.framedir):
        edit_frame(opt.framedir, opt.prefix)
    else:
        frame_files = []

        for f in os.listdir(opt.framedir):
            split_tup = os.path.splitext(f)

            fname = os.path.join(opt.framedir, f)
            if os.path.isfile(fname) and split_tup[1] == ".png":
                frame_files.append(fname)

        print(f">>Found {len(frame_files)} frames to edit in dir '{opt.framedir}'")

        BG_COLOR = (192, 192, 192) # gray
        with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5) as pose:

            for idx, file in enumerate(frame_files):
                image = cv2.imread(file)
                image_height, image_width, _ = image.shape
                # Convert the BGR image to RGB before processing.
                results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

                if not results.pose_landmarks:
                    continue
                else:
                    print(f'Nose coordinates: ('
                        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
                        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
                    )
