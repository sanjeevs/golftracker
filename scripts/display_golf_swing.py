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

    start_idx = gs.pose_sequence[0]
    finish_idx = gs.pose_sequence[1]
    if start_idx == None or finish_idx == None:
        print(f">>Could not detect the start or end pose. Run 'label_golf_poses' and 'create_swing_db'")
        sys.exit(1)
    
    print(f">>Video file is {gs.video_input.fname} with start_idx={start_idx} and finish_idx={finish_idx}")

    frames = video_frames[start_idx : finish_idx + 1]
    frame_shape = video_frames[0].shape

    # Check if club head detection has run.
    # if gs.computed_club_head_points[0] == None:
    #     print(f">>Club head detection not yet run....Running it")
    #     gs.run_club_head_detection(frames)

    out_frames = []
    for i in range(len(frames)):
        out_frames.append(np.zeros(frame_shape, dtype=np.uint8))

    mp_frames = copy.deepcopy(frames)
    for i in range(len(mp_frames)):
        gs.draw_frame(i, out_frames[i])
        gs.draw_frame(i, mp_frames[i])

    canny_frames = copy.deepcopy(frames) #gs.canny_edge_gen.run(frames)
    right_thumb_path = path_model.get_path(gs, "right_shoulder")
    for i, f in enumerate(canny_frames):
        canny_frames[i] = cv2.circle(f, right_thumb_path[i], 5, color=(255, 0, 0), thickness=-1)

    lines_frames = copy.deepcopy(frames)
    # for idx in range(len(lines_frames)):
    #     for line in gs.hough_lines[idx]:
    #         pt1 = (line[0], line[1])
    #         pt2 = (line[2], line[3])
    #         cv2.line(lines_frames[idx], pt1, pt2, (0, 0, 255))

    #cv2.namedWindow("LabelPoses")
    print(f"Found {len(mp_frames)} frames with starting pose")


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

            
            #points = gs.get_mp_points(idx, gs.height, gs.width)

            model_img = copy.deepcopy(mp_frames[idx])
            #model_img = double_pendlum.draw(blank_img, points)
            club_line = None #gs.get_club_line(idx)
            if club_line:
                model_img = cv2.line(model_img, (club_line[0], club_line[1]), 
                                                (club_line[2], club_line[3]),
                                                color=(0, 0, 255), thickness=3)

            #line_img = copy.deepcopy(mp_frames[idx])
            
            if opt.stack > 2:
                img_array = [[None, None], [None, None]]
                labels = [[None, None], [None, None]]
                img_array[0][0] = video_frames[idx]
                labels[0][0] = f"Frame{idx}"
                img_array[0][1] = out_frames[idx]
                labels[0][1] = f"{gs.get_golf_pose(idx)}"
                img_array[1][0] = canny_frames[idx]
                labels[1][0] = "CannyEdge"
                img_array[1][1] = lines_frames[idx]
                labels[1][1] = "HoughLines"

                stacked_images = image_utils.stack_images(imgArray=img_array,
                  scale=0.4, labels=labels)
             
            elif opt.stack == 2:
                img_array = [[None, None]]
                labels = [[None, None]]
                img_array[0][0] = video_frames[idx]
                labels[0][0] = f"Frame{idx}"
                img_array[0][1] = out_frames[idx]
                labels[0][1] = f"{gs.get_golf_pose(idx)}"
            else:
                img_array = [[None]]
                labels = [[None]]
                img_array[0][0] = video_frames[idx]
                labels[0][0] = f"Frame{idx}"

            stacked_images = image_utils.stack_images(imgArray=img_array,
                labels=labels, scale=opt.scale/100)
                     
            cv2.imshow("StackedImages", stacked_images)

            
            key_pressed = cv2.waitKey(-1) & 0xff
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
