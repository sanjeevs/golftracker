"""
Dump the selected screen coordinates to a csv file.
"""
import numpy as np
import cv2
import argparse
import logging
import os
import copy


from golftracker import golf_swing_repository
from golftracker import golf_swing
from golftracker import club_head_params
from golftracker import club_head_detector

from golftracker import video_utils

img = None
frame_idx = 0
points_dict = {}


def put_msg(frame, msg):
    width = int(frame.shape[1])
    height = int(frame.shape[0])

    cv2.rectangle(frame, (0, 0), (width, 73), (245, 117, 16), -1)
    cv2.putText(
        frame,
        msg,
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )


def click_event(event, x, y, flags, params):
    global img
    global frame_idx
    global points_dict

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + "," + str(y), (x, y), font, 1, (255, 0, 0), 2)
        points_dict[frame_idx] = (x, y)
        cv2.imshow("Default", img)


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Label the club head position in pkl data base"
    )

    parser.add_argument("swing_db", type=str, help="Input golf swing data base")
    parser.add_argument("-f", "--force", action='store_true', 
            help="Overwrite the club head pos in pkl db")
    return parser


def main():
    global img
    global frame_idx
    global points_dict

    logging.basicConfig(level=os.environ.get("LOGCLEVEL", "INFO"))
    opt = create_parser().parse_args()

    gs = golf_swing_repository.reconstitute(opt.swing_db)
    print(f">>Video file is {gs.video_input.fname}")
    video_frames = gs.get_video_frames()
    
    cv2.namedWindow("Default")
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback("Default", click_event)

    points_dict = {}
    for frame_idx in range(len(video_frames)):
        img = video_frames[frame_idx]
        pose = gs.get_golf_pose(frame_idx)
        put_msg(img, f"Fr {frame_idx}:{pose.name}")
        cv2.imshow("Default", img)
        key_pressed = cv2.waitKey(-1) & 0xFF
        if key_pressed == ord("q") or key_pressed == 27:
            break

    cv2.destroyAllWindows()

    ch_params = club_head_params.ClubHeadParams()
    ch_params.club_head_points_dict = points_dict
    ch_detector = club_head_detector.ClubHeadDetector(ch_params)
    ch_result = ch_detector.run(gs)

    if opt.force:
        gs.club_head_result.reset_and_update(ch_result)
    else:
        gs.club_head_result.update(ch_result)

    golf_swing_repository.serialize(opt.swing_db, gs)

if __name__ == "__main__":
    main()
