"""
Dump the selected screen coordinates to a csv file.
"""
import numpy as np
import cv2
import argparse
import logging
import os
import copy
import os

from golftracker import golf_swing_repository
from golftracker import golf_swing
from golftracker import club_head_params
from golftracker import club_head_detector
from golftracker import gt_const as gt
from golftracker import image_utils, file_utils


#------------------------
# Global variables
# ------------------------
img = None
frame_idx = 0
points_dict = {}

def click_event(event, x, y, flags, params):
    global img
    global frame_idx
    global points_dict

    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + "," + str(y), (x, y), font, 1, 
            image_utils.BGR_VALUES['light_gray'], 2)
        points_dict[frame_idx] = (x, y)
        cv2.imshow("LabelClubHead", img)


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Label the club head position in pkl data base"
    )

    parser.add_argument("swing_db", type=str, help="Input golf swing data base")
    parser.add_argument("-s", "--step", type=int, default=5, 
            help="Increment for the jump key." )
    parser.add_argument("-f", "--force", action='store_true', 
            help="Overwrite the club head pos in pkl db")
    parser.add_argument("--state", type=str, default="", help="input state file")
    parser.add_argument("--init", action="store_true", help="init the result first.")
    parser.add_argument("--scale", default=100, type=int,
        help="resize the incoming video file by scale percent",
    )
    parser.add_argument("--rotate", default=0, type=int,
        help="rotate the incoming video file",
    )
    return parser


def main():
    global img
    global frame_idx
    global points_dict

    logging.basicConfig(level=os.environ.get("LOGCLEVEL", "INFO"))
    opt = create_parser().parse_args()

    gs = golf_swing_repository.reconstitute(opt.swing_db)
    print(f">>Loading video file is {gs.video_input.fname}")
   
   
    if opt.init:
        print(f">>Init the club head result in swing.")
        gs.init_club_head_result()
        golf_swing_repository.serialize(opt.swing_db, gs)
        return

    video_frames = gs.get_video_frames(scale=opt.scale, rotate=opt.rotate)
    cv2.namedWindow("LabelClubHead")
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback("LabelClubHead", click_event)

    points_dict = {}
    while frame_idx < len(video_frames):
        img = video_frames[frame_idx]
        pose = gs.get_golf_pose(frame_idx)
        ch_pt, ch_source = gs.get_club_head_info(frame_idx)
        msg = f"Fr{frame_idx}:{gt.abbrev_pose(pose)}:{ch_source}"
        image_utils.put_msg(img, msg)
        if ch_pt is not None:
            if ch_source == "Label":
                cv2.circle(img, ch_pt, 5, image_utils.BGR_VALUES['red'], -1)
            else:
                cv2.circle(img, ch_pt, 5, image_utils.BGR_VALUES['yellow'], -1)
        cv2.imshow("LabelClubHead", img)

        # Key handling
        key_pressed = cv2.waitKey(-1) & 0xFF
        if key_pressed == ord('j'):
            frame_idx = min(frame_idx + opt.step, len(video_frames) -1)
        elif key_pressed == ord('n') or key_pressed == 32:  #spacebar
            frame_idx = min(frame_idx + 1, len(video_frames) -1)
        elif key_pressed == ord('p'):
            frame_idx = max(frame_idx - 1, 0)
        elif key_pressed == ord("q") or key_pressed == 27:
            break
        else:
            print(f"Ignore key pressed. Valid keys are 'j, n/spacebar, p, q/esc'")
    cv2.destroyAllWindows()

    
    ch_params = club_head_params.ClubHeadParams()
    ch_params.club_head_points_dict = points_dict
    ch_detector = club_head_detector.ClubHeadDetector(ch_params)
    ch_result = ch_detector.run(gs)

    if opt.state and os.path.exists(opt.state):
        print(f">>Reading club head state from '{opt.state}'")
        _ , lst = file_utils.read_from_csv(opt.state, has_header=True)
        gs.club_head_result.import_lst(lst)

    if opt.force:
        gs.club_head_result.reset_and_update(ch_result)
    else:
        gs.club_head_result.update(ch_result)

    print(f">>Saving golf database to '{opt.swing_db}'")
    golf_swing_repository.serialize(opt.swing_db, gs)
    if opt.state:
        print(f">>Saving club head state to '{opt.state}'")
        header, lst = gs.club_head_result.export_lst()
        file_utils.write_to_csv(lst, opt.state, header=header)

    

if __name__ == "__main__":
    main()
