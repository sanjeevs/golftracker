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
    if start_idx == None or finish_idx == None:
        print(f">>Could not detect the start or end pose. Run 'label_golf_poses' and 'create_swing_db'")
        sys.exit(1)
    
    print(f">>Video file is {gs.video_fname} with start_idx={start_idx} and finish_idx={finish_idx}")

    frames = video_frames[start_idx : finish_idx + 1]
    frame_shape = video_frames[0].shape

    # Check if club head detection has run.
    if gs.computed_club_head_points[0] == None:
        print(f">>Club head detection not yet run....Running it")
        gs.run_club_head_detection(frames)

    sw_frames = []
    for i in range(len(frames)):
        sw_frames.append(np.zeros(frame_shape, dtype=np.uint8))

    mp_frames = copy.deepcopy(frames)
    for i in range(len(mp_frames)):
        gs.draw_frame(i, sw_frames[i])
        gs.draw_frame(i, mp_frames[i])

    canny_frames = gs.canny_edge_gen.run(frames)
    lines_frames = copy.deepcopy(frames)
    for idx in range(len(lines_frames)):
        for line in gs.hough_lines[idx]:
            pt1 = (line[0], line[1])
            pt2 = (line[2], line[3])
            cv2.line(lines_frames[idx], pt1, pt2, (0, 0, 255))

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

            #line_img = copy.deepcopy(mp_frames[idx])
            
            stacked_images = image_utils.stack_images(([video_frames[idx], sw_frames[idx]], 
                                                       [canny_frames[idx], lines_frames[idx]]), scale=0.4,
                                                       labels=([f"Frame{idx}", f"{gs.get_golf_pose(idx)}"],
                                                               ["CannyImg", "HoughLines"]))
            cv2.imshow("StackedImages", stacked_images)
            key_pressed = cv2.waitKey(-1) & 0xff
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
