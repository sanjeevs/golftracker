import numpy as np
import cv2
import argparse
import logging
import os
import copy
import sys

from golftracker import golf_swing_repository
from golftracker import video_utils
from golftracker import image_utils
from golftracker import path_model
from golftracker import gt_const 


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Display the golf swing from the pkl data base"
    )

    parser.add_argument("swing_db", type=str, help="Input golf swing data base")
    parser.add_argument("--stack", type=int, default=2, help="Shows '1/2/4' stacked images ")
    parser.add_argument("--scale", type=int, default=75, help="scales the stacked images in pcnt")

    return parser


def main():
    logging.basicConfig(level=os.environ.get("LOGCLEVEL", "INFO"))
    opt = create_parser().parse_args()
    gs = golf_swing_repository.reconstitute(opt.swing_db)
    
    video_frames = gs.get_video_frames()
            
    start_idx, finish_idx = gs.get_golf_pose_sequence()
    if start_idx == None or finish_idx == None:
        print(f">>Could not detect the start or end pose. Run 'label_golf_poses' and 'create_swing_db'")
        sys.exit(1)
    
    print(f">>Video file is {gs.video_input.fname} with start_idx={start_idx} and finish_idx={finish_idx}")

    frames = video_frames[start_idx : finish_idx + 1]
    frame_shape = video_frames[0].shape

    # out canvas to draw the computed images
    background = []
    for i in range(len(frames)):
        background.append(np.zeros(frame_shape, dtype=np.uint8))

    # Output to compute.
    mp_frames = copy.deepcopy(background)
    for i in range(len(mp_frames)):
        gs.draw_frame(i, mp_frames[i])

    time_lapses = copy.deepcopy(background)
    for i in range(len(frames)):
        gs.draw_frame(i, time_lapses[i], line_color="blue")
        gs.draw_frame(start_idx, time_lapses[i], line_color="pale_blue")
    
    if len(mp_frames) > 0:
        idx = start_idx
        key_pressed = ''

        print(f">> Press 'q' OR Esc to return")
        while key_pressed != ord('q') and key_pressed != 27: # Esc key

            if key_pressed == ord('p'):
                # Previous frame
                idx = max(idx -1, start_idx)
                
            if key_pressed == ord('n') or key_pressed == 32:
                # Next frame
                idx = min(idx + 1, finish_idx)

            images = [
                    (video_frames[idx], f"Frame {idx}"),
                    mp_frames[idx],
                    (time_lapses[idx], f"Lapse {idx}"),
                    (mp_frames[idx], f"{gs.get_golf_pose(idx)}")
            ]

            stacked_images = image_utils.stack_images(images=images, scale=opt.scale/100, 
                    num_windows=opt.stack)
            
            cv2.imshow("StackedImages", stacked_images)

            
            key_pressed = cv2.waitKey(-1) & 0xff
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
