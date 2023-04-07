import numpy as np
import cv2
import argparse
import logging
import os
import copy


from golftracker import golf_swing_repository
from golftracker import video_utils
from golftracker import image_utils

from golftracker import gt_const 
from golftracker import double_pendlum

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Display the golf swing from the pkl data base"
    )

    parser.add_argument("swing_db", type=str, help="Input golf swing data base")

    return parser


def main():
    logging.basicConfig(level=os.environ.get("LOGCLEVEL", "INFO"))
    opt = create_parser().parse_args()
    gs = golf_swing_repository.reconstitute(opt.swing_db)
    
    (video_frames, _) = video_utils.split_video_to_frames(gs.video_fname)

    start_idx = gs.pose_sequence[0]
    finish_idx = gs.pose_sequence[1]
    print(f">>Video file is {gs.video_fname} with start_idx={start_idx} and finish_idx={finish_idx}")

    frames = video_frames[start_idx : finish_idx + 1]
    frame_shape = video_frames[0].shape

    club_lines = [] #club_detection.run(gs, frames)


    sw_frames = []
    for i in range(len(frames)):
        sw_frames.append(np.zeros(frame_shape, dtype=np.uint8))

    mp_frames = copy.deepcopy(frames)
    for i in range(len(mp_frames)):
        gs.draw_frame(i, sw_frames[i])
        gs.draw_frame(i, mp_frames[i])

    #cv2.namedWindow("LabelPoses")
    print(f"Found {len(mp_frames)} frames with starting pose")


    if len(mp_frames) > 0:
        idx = start_idx
        key_pressed = ''

        print(f">> Press 'q' OR Esc to return")
        while key_pressed != ord('q') and key_pressed != 27: # Esc key

            if key_pressed == ord('p'):
                # Previous frame
                idx -= 1
                

            if key_pressed == ord('n') or key_pressed == 32:
                # Next frame
                idx += 1

            # Sanitize
            if(idx < start_idx) :
                idx = start_idx
            if (idx >= finish_idx):
                idx = finish_idx

                
            points = gs.get_mp_points(idx, gs.height, gs.width)

            model_img = copy.deepcopy(mp_frames[idx])
            #model_img = double_pendlum.draw(blank_img, points)
            club_line = None #gs.get_club_line(idx)
            if club_line:
                model_img = cv2.line(model_img, (club_line[0], club_line[1]), 
                                                (club_line[2], club_line[3]),
                                                color=(0, 0, 255), thickness=3)

            line_img = copy.deepcopy(mp_frames[idx])
           
            stacked_images = image_utils.stack_images(([video_frames[idx], sw_frames[idx]], 
                                                       [model_img, line_img]), scale=0.6,
                                                       labels=([f"Frame{idx}", "SWView"],
                                                               ["LabelClub", f"{gs.get_golf_pose(idx)}"]))
            cv2.imshow("StackedImages", stacked_images)
            key_pressed = cv2.waitKey(-1) & 0xff
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
