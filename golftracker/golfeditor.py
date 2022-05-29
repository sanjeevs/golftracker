"""Editor to mark the various trackers by hand."""

import argparse
import os.path
import cv2

from golftracker import tracker
from golftracker import draw

def create_parser():
    """"Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Editor for user to select the various trackers."
    )
    parser.add_argument("--json", "-j", default="", help="Name for json file(s).")
    parser.add_argument("frame", type=str, help="Frame or dir holding all the frames.")
    return parser


gui_state = "BALL"  # Other states are SHAFT
frame_tracker = tracker.Tracker()


def mouse_event_handler(event, x, y, flags, frame):
    """Event handler to detect mouse clicks."""
    if event == cv2.EVENT_LBUTTONDOWN:
        if gui_state == "BALL":
            frame_tracker.update_ball(x, y)
        elif gui_state == "SHAFT":
            frame_tracker.update_shaft(x, y)

        draw.draw_tracker(frame, frame_tracker)
        cv2.imshow("main", frame)

def tag_frame(frame):
    """Tag the tracker in the frame.
    :param frame : Input frame to draw the tracker.
    :return Json representation of the trackers.
    """
    global frame_tracker, gui_state
    frame_tracker = tracker.Tracker()
    gui_state = "BALL"

    while True:
        key_pressed = cv2.waitKey(0) & 0xFF
        if key_pressed == ord("q"):
            break
        elif key_pressed == ord("b"):
            gui_state = "BALL"
        elif key_pressed == ord("s"):
            gui_state = "SHAFT"

    return frame_tracker.to_json()


def main():
    """Main program"""
    opt = create_parser().parse_args()

    cv2.namedWindow(winname="main", flags=cv2.WINDOW_NORMAL)


    if os.path.isfile(opt.frame):
        frame = cv2.imread(opt.frame)
        cv2.imshow("main", frame)
        cv2.setMouseCallback("main", mouse_event_handler, frame)

        json_str = tag_frame(frame)

        json_fname = "my.json"
        with open(json_fname, "w") as fh:
            fh.write(json_str)

    else:
        print(f">>Working on frames in dir '{opt.frame}'")

    cv2.destroyWindow("main")
