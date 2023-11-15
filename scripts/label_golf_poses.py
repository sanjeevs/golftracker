# Script
# User labels the different golf poses.
# The poses are enum defined in golftracker/gt_const


import argparse
import cv2
import os
import pickle
import numpy as np
import mediapipe as mp
import csv

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

from golftracker import gt_const as gt 
from golftracker import video_utils
from golftracker import golf_swing_repository
from collections import defaultdict


KEY_STATE_ENCODING = { ord('s'): "Start golf pose", 
                        ord('t'): "Top golf pose", 
                        ord('f'): "Finish golf pose" }

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Label the different golf poses in the video."
    )

    parser.add_argument(
        "swing_db", type=str, help="Input swing pkl database"
    )

    parser.add_argument(
        "--type",
        "-t",
        default='right',
        type=str,
        help="Set to right/left handedness of the player"
    )

    parser.add_argument(
        "--out",
        "-o",
        default='',
        type=str,
        help="Output csv file name. Append if it exists"
    )

    parser.add_argument(
        "--scale",
        "-s",
        default=100,
        type=int,
        help="resize the incoming video file by scale percent",
    )

    parser.add_argument(
        "--rotate", 
        "-r", 
        default="", help="rotate the incoming video file",
    )

    return parser

def put_msg(frame, msg):
    width = int(frame.shape[1])
    height = int(frame.shape[0])

    cv2.rectangle(frame, (0, 0), (width, 73), (245, 117, 16), -1)
    cv2.putText(frame, msg, 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

    cv2.rectangle(frame, (0, height -40), (width, height), (245, 117, 16), -1)
    cv2.putText(frame, "s:start, t:top, f:finish", 
                    (10, height -10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)


def is_pose_key_detected(key_pressed):
    """ Return true if the user pressed a pose class change."""
    return key_pressed in KEY_STATE_ENCODING.keys()
  
def create_pose_class(key_pressed, handedness):
    if key_pressed == ord('s'):
        return gt.GolfPose.LhStart if handedness == "left" else gt.GolfPose.RhStart
    elif key_pressed == ord('t'):
        return gt.GolfPose.LhTop if handedness == "left" else gt.GolfPose.RhTop
    elif key_pressed == ord('f'):
        return gt.GolfPose.LhFinish if handedness == "left" else gt.GolfPose.RhFinish
    else:
        return None


def save_pose_coordinates_to_csv(fname, mode, golfswing, pose_classes):
    """ Save golf poses to csv fname. """

    num_coords = len(gt.MP_POSE_LANDMARKS)
    landmarks = ['class']
    for val in range(1, num_coords+1):
        landmarks += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val), 'v{}'.format(val)]

    with open(fname, mode=mode, newline='') as fh:
        csv_writer = csv.writer(fh, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if mode == "w":
            csv_writer.writerow(landmarks)

        for idx, golf_pose in pose_classes.items():
            if golf_pose:
                pose_row = golfswing.get_mp_landmarks_flat_row(idx)
              
                # Append class name 
                pose_row.insert(0, golf_pose)
            
                csv_writer.writerow(pose_row)


def main():
    opt = create_parser().parse_args()

    for key in KEY_STATE_ENCODING.keys():
        print(f"KeyPressed '{chr(key)}'' ==> {create_pose_class(key, opt.type)}: {KEY_STATE_ENCODING[key]}")

    if opt.out == "":
        opt.out = os.path.basename(opt.swing_db).split('.')[0] + ".csv"

    gs = golf_swing_repository.reconstitute(opt.swing_db)
    frames = gs.get_video_frames()

    for i in range(gs.num_frames):
        gs.draw_frame(i, frames[i])

    # -----------------------------------------------
    # Loop  for user to select the type of golf pose
    #----------------------------------------------------       
    pose_classes = {}

    cv2.namedWindow("LabelPoses")
  
    if len(frames) > 0:
        idx = 0
        key_pressed = ''

        print(f">> Press 'q' to save to csv OR Esc to return")
        while key_pressed != ord('q') and key_pressed != 27: # Esc key
            
            frame = frames[idx]

            if key_pressed == ord('p'):
                # Previous frame
                idx -= 1
                

            if key_pressed == ord('n') or key_pressed == 32:
                # Next frame
                idx += 1

            # Sanitize
            if(idx < 0) :
                idx = 0
            if (idx >= len(frames)):
                idx = len(frames) -1

            if is_pose_key_detected(key_pressed):
                pose_classes[idx] = create_pose_class(key_pressed, opt.type).name
                put_msg(frames[idx], f"Fr{idx}:{pose_classes[idx]}")
            else:
                put_msg(frames[idx], f"Fr{idx}")


            cv2.imshow("LabelPoses", frames[idx])
            key_pressed = cv2.waitKey(-1) & 0xff
    
    if key_pressed == 27:  #Esc key to abort the save
        print(f">>Escape key detected. Not saving any pose data")
        pose_classes = {}

    else:
        hist = defaultdict(list)
        for k, v in pose_classes.items():
            hist[v].append(k)

        for k, v in hist.items():
            print(f">>{k} in frames={v}")

       
        print(f"\n>> Creating {len(pose_classes)} labels in '{opt.out}' for '{opt.swing_db}'")
        save_pose_coordinates_to_csv(opt.out, "w", gs, pose_classes)

        print(f"\n>> Run the cmd 'train_posemodel -f <model_pkl> {opt.out}' to train model.")
        print(f">> Default: train_posemodel -f {os.path.join('..', 'model', 'pose_models.pkl')} "
                f" {opt.out}")

        

    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
