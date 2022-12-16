# Script
# Uses the ML model to predict the golf poses.

import argparse
import cv2
import os
import numpy as np
import mediapipe as mp
import csv
import pickle
import pandas as pd

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

from golftracker import video_utils
from collections import defaultdict


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Predict the poses in a golf video")

    parser.add_argument("model", type=str, help="ML model in pkl format")

    parser.add_argument("video", type=str, help="Input video file")

    parser.add_argument(
        "--scale",
        "-s",
        default=100,
        type=int,
        help="resize the incoming video file by scale percent",
    )

    parser.add_argument(
        "--rotate", "-r", default="", help="rotate the incoming video file",
    )

    parser.add_argument(
        "--threshold", "-t", default=60, type=int, help="Threshold for model preidction",
    )
    return parser


def put_msg(frame, pose_class, pose_prob):
    width = int(frame.shape[1])
    height = int(frame.shape[0])

    cv2.rectangle(frame, (0, 0), (width, 73), (245, 117, 16), -1)
    cv2.putText(
        frame,
        pose_class,
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    cv2.rectangle(frame, (0, height - 40), (width, height), (245, 117, 16), -1)
    cv2.putText(
        frame,
        f"{pose_prob}",
        (10, height - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )


def main():
    opt = create_parser().parse_args()

    with open(opt.model, "rb") as f:
        model = pickle.load(f)

    frames = video_utils.split_video_to_frames(opt.video, opt.scale, opt.rotate)

    # -----------------------------------------------
    # Run ml model through each frame.
    # ----------------------------------------------------

    if len(frames) > 0:
        idx = 0
        key_pressed = ""

        while key_pressed != ord("q") and idx < len(frames):

            frame = frames[idx]

            if key_pressed == ord("p"):
                # Previous frame
                idx -= 1

            if key_pressed == ord("n") or key_pressed == 32:
                # Next frame
                idx += 1

            # Sanitize
            if idx < 0:
                idx = 0
            if idx >= len(frames):
                idx = len(frames) - 1

            with mp_pose.Pose(
                static_image_mode=True,
                model_complexity=1,
                enable_segmentation=True,
                min_detection_confidence=0.5,
            ) as pose:

                results = pose.process(frame)
                dis_frame = frame.copy()
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(
                        dis_frame,
                        results.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                        mp_drawing.DrawingSpec(
                            color=(245, 117, 66), thickness=2, circle_radius=2
                        ),
                        mp_drawing.DrawingSpec(
                            color=(245, 66, 230), thickness=2, circle_radius=2
                        ),
                    )

                pose = results.pose_landmarks.landmark
                pose_row = list(
                    np.array(
                        [
                            [landmark.x, landmark.y, landmark.z, landmark.visibility]
                            for landmark in pose
                        ]
                    ).flatten()
                )

                 # Make Detections
                X = pd.DataFrame([pose_row])
                pose_class = model.predict(X)[0]
                pose_prob = model.predict_proba(X)[0]
                max_prob = round(pose_prob[np.argmax(pose_prob)], 2)

                if (max_prob * 100) > opt.threshold:
                    put_msg(dis_frame, f"Fr:{idx}:{pose_class}", str(max_prob))
                else:
                    put_msg(dis_frame, f"Fr:{idx}:", str(max_prob))

                cv2.imshow("PredictModel", dis_frame)
                key_pressed = cv2.waitKey(-1) & 0xFF


if __name__ == "__main__":
    main()
