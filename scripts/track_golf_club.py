# Track the golf club in a golf swing video

import argparse
import os
import pickle
import cv2


from golftracker import club_detection
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
    rh_start_idxs = gs.get_pose_frames(gt.GolfPose.RhStart)
    print(f">>Found {len(rh_start_idxs)} starting pose frames")
    frames  = gs.get_video_frames()

    club_line = None
    #for frame_idx in rh_start_idxs:
    for frame_idx in range(len(frames)):
        frame = frames[frame_idx]
        print(f">>Detecting club in frame idx={frame_idx}")
        club_line = club_detection.detect_club_in_start_pose(gs, frame_idx, frame)
        if club_line:
            print(f"club_line={club_line}")
            img = cv2.line(frame, (club_line[0], club_line[1]), (club_line[2], club_line[3]), (0, 255, 0), thickness=3)
        else:
            img = frame
        cv2.imshow("GolfClub", img)
        cv2.waitKey(8)
            

    cv2.destroyAllWindows()

    if club_line:
        img = convert_frame(frames[frame_idx])
        tracker = cv2.legacy.TrackerMedianFlow_create()
        x, y = club_line[0] -3, club_line[1] - 3
        w, h = 10, 10
        tracker.init(img, [x, y, w, h])

        for i in range(len(frames)):
            if i > frame_idx:
                img = convert_frame(frames[i])
                print(img.shape)
                ok, bbox = tracker.update(img)
                if ok:
                    x, y , w, h = bbox
                    p1 = (int(x), int(y))
                    p2 = (int(x + w), int(y + h))
                    tmp = cv2.rectangle(img, p1, p2, (0, 255, 0), 3)
                else:
                    print(f"tracking failed at frame {i}")
                cv2.imshow("Tracking", img)
                cv2.waitKey(0)    

    cv2.waitKey()
    cv2.destroyAllWindows()