"""Editor to mark the various trackers by hand."""

import argparse
import os
import os.path
import cv2

from golftracker import tracker
from golftracker import draw


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Editor for user to select the various trackers."
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

frame_tracker = tracker.Tracker()
tracker_selected = "BALL"  # Other states are SHAFT
orig_frame = None

def show_frame_main():
    """ Display a copy of the orig frame with the messages."""
    h, w, c = orig_frame.shape
    temp = orig_frame.copy()
    f = cv2.putText(temp, tracker_selected, (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2, cv2.LINE_AA)

    draw.draw_tracker(f, frame_tracker)
    cv2.imshow("main", f)

def mouse_event_handler(event, x, y, flags, frame):
    """Event handler to detect mouse clicks.
    Handles left button down click. The currently selected tracker is maintained
    in a global variable.

    """
    if event == cv2.EVENT_LBUTTONDOWN:
        if tracker_selected == "BALL":
            frame_tracker.update_ball(x, y)
        elif tracker_selected == "SHAFT":
            frame_tracker.update_shaft(x, y)
        else:
            raise IndexError(f"Unknown tracker state '{tracker_selected}'")
        show_frame_main()

def process_key_pressed():
    """Process key stroke and set the gui state and trackers.
    Currently only tracking the ball and club shaft position.

    """
    global frame_tracker, tracker_selected
    frame_tracker = tracker.Tracker()

    while True:
        key_pressed = cv2.waitKey(0) & 0xFF
        if key_pressed == ord("q"):
            nxt_state  = "QUIT"
            break
        elif key_pressed == ord('n'):
            nxt_state = "NEXT"
            break
        elif key_pressed == ord('p'):
            nxt_state = "PREV"
            break
        elif key_pressed == ord('j'):
            nxt_state = "JUMP"
            break
        elif key_pressed == ord('u'):
            nxt_state = "UNDO"
            frame_tracker = tracker.Tracker()  #Reset tracker
            break
        elif key_pressed == ord("b"):
            tracker_selected = "BALL"          #Work on the current frame
            show_frame_main()
        elif key_pressed == ord("s"):
            tracker_selected = "SHAFT"
            show_frame_main()

    return nxt_state

def edit_frame(frame_fname, json_prefix, msg):
    """Edit the frame fname and store the result in the json file.

    :param frame_fname: Frame filename.
    :param json_prefix: Prefix added to json filename.
    :param msg: Message to display on the frame

    :return next state: Indicates whether to go to next/prev frame.
    """
    json_fname = os.path.splitext(frame_fname)[0] + ".json"
    frame = cv2.imread(frame_fname)

    #
    # Prepare the global variables for the show.
    #
    global orig_frame
    orig_frame = cv2.putText(frame, msg, (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 255), 2, cv2.LINE_AA)
    global frame_tracker
    frame_tracker = tracker.Tracker()  # Reset the tracker

    #
    # Display the frame and setup the callbacks.
    #
    show_frame_main()
    cv2.setMouseCallback("main", mouse_event_handler, frame)

    nxt_state = process_key_pressed()

    json_str = frame_tracker.to_json()
    if json_str:
        with open(json_fname, "w") as fh:
            fh.write(json_str)

    return nxt_state


def main():
    """Main program"""
    opt = create_parser().parse_args()
  
    cv2.namedWindow(winname="main", flags=cv2.WINDOW_NORMAL)

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

        idx = 0
        while True:
            idx = idx % len(frame_files)
            f = frame_files[idx]
            nxt_state = edit_frame(f, opt.prefix,
                                   f"{idx}/{len(frame_files)}. Press n-next, p-prev, j-jump10 u-undo q-quit")
            if nxt_state == "QUIT":
                break
            elif nxt_state == "NEXT":
                idx += 1
            elif nxt_state == "PREV":
                if idx > 0:
                    idx -= 1
            elif nxt_state == "JUMP":
                idx += 10
            elif nxt_state == "UNDO":
                pass
            else:
                raise IndexError(f"Unknown value of nxt_state={nxt_state}")

    cv2.destroyWindow("main")
