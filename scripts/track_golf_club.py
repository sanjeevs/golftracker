# Track the golf club in a golf swing video

import argparse
import os
import pickle
import cv2


from golftracker import club_head_detection
from golftracker import golf_swing_repository
from golftracker import gt_const as gt

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(description="Track the golf club in swing database")

    parser.add_argument("db", type=str, help="Swing database")
    return parser

def convert_frame(frame):
 # Run canny edge detection
    low_threshold = 50
    high_threshold = 150
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    img = cv2.merge((edges, edges, edges))
    return  img


def main():
    opt = create_parser().parse_args()
    
    gs = golf_swing_repository.reconstitute(opt.db)
    frames  = gs.get_video_frames()

    club_line = None
    #for frame_idx in rh_start_idxs:
    for frame_idx in range(len(frames)):
        frame = frames[frame_idx]
        lines = gs.run_hg_line_detection(frame)
        club_lines = gs.filter_frame_lines(frame_idx, lines)
        if club_lines:
            club_line = club_lines[0]
            img = cv2.line(frame, (club_line[0], club_line[1]), 
                    (club_line[2], club_line[3]), (0, 255, 0), thickness=3)
        else:
            img = frame
        cv2.imshow("GolfClub", img)
        cv2.waitKey(-1)
            

    cv2.destroyAllWindows()