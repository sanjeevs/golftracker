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
import copy

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

from golftracker import gt_const as gt 
from golftracker import video_utils,image_utils
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

    return parser



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

def main():
    opt = create_parser().parse_args()

    for key in KEY_STATE_ENCODING.keys():
        print(f"KeyPressed '{chr(key)}'' ==> {create_pose_class(key, opt.type)}: {KEY_STATE_ENCODING[key]}")

    if opt.out == "":
        opt.out = "pose_" + os.path.basename(opt.swing_db).split('.')[0] + ".csv"

    gs = golf_swing_repository.reconstitute(opt.swing_db)
    frames = gs.get_video_frames(opt.scale)

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
                pose = create_pose_class(key_pressed, opt.type)
                gs.set_golf_pose(idx, pose)

            pose = gs.get_golf_pose(idx)
            frame = copy.deepcopy(frames[idx])
            image_utils.put_msg(frame, f"Fr{idx}:{pose.name}")
            cv2.imshow("LabelPoses", frame)
            key_pressed = cv2.waitKey(-1) & 0xff

    cv2.destroyAllWindows()
    print(f">>Saving golf database to '{opt.swing_db}'")
    golf_swing_repository.serialize(opt.swing_db, gs)
if __name__ == "__main__":
    main()
