'''
Dump the selected screen coordinates to a csv file.
'''
import numpy as np
import cv2
import argparse
import logging
import os
import copy


from golftracker import golf_swing_repository
from golftracker import video_utils

img = None
frame_idx = 0
points = {}


def put_msg(frame, msg):
    width = int(frame.shape[1])
    height = int(frame.shape[0])

    cv2.rectangle(frame, (0, 0), (width, 73), (245, 117, 16), -1)
    cv2.putText(frame, msg, 
                    (10,60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

def click_event(event, x, y, flags, params):
    global img
    global frame_idx
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        points[frame_idx] = (x, y)
        cv2.imshow('Default', img)
        

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Display the golf swing from the pkl data base"
    )

    parser.add_argument("swing_db", type=str, help="Input golf swing data base")
    parser.add_argument("-o", "--out", type=str, default="", help="Coordinates of points selected")

    return parser

def main():
    global img
    global frame_idx
    global points

    logging.basicConfig(level=os.environ.get("LOGCLEVEL", "INFO"))
    opt = create_parser().parse_args()
    gs = golf_swing_repository.reconstitute(opt.swing_db)
    print(f">>Video file is {gs.video_fname}")
    (video_frames, _) = video_utils.split_video_to_frames(gs.video_fname)

    cv2.namedWindow("Default")
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('Default', click_event)

    points = {}
    for frame_idx in range(len(video_frames)):
        img = video_frames[frame_idx]
        pose = gs.get_golf_pose(frame_idx)
        put_msg(img, f"Fr {frame_idx}:{pose.name}")
        cv2.imshow("Default", img)
        key_pressed = cv2.waitKey(-1) & 0xff
        if key_pressed == ord('q') or key_pressed == 27:
            break

    cv2.destroyAllWindows()

    ans = input(f">>> Do you want to update the pkl file '{opt.swing_db}'  (y/n) ")
    if ans == "yes" or ans == 'y' or ans == 'Y' or ans == '':
        print(f">>Updating {len(points)} points '{opt.swing_db}' file")
        for key, value in points.items():
            gs.set_club_head_point(key, value)
        golf_swing_repository.serialize(opt.swing_db, gs)
    else:
        print(f">>SKIP updating the pkl filke '{opt.swing_db}'")

    if opt.out:
        print(f">>Writing {len(points)} points to output csv file '{opt.out}'")
        with open(opt.out, "w") as csvfile:
            for key, value in points.items():
                csvfile.write(f"{key}, {value[0]}, {value[1]}\n")


if __name__ == "__main__":
    main()