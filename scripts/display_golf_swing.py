import numpy as np
import cv2
import argparse
import logging
import os
import copy


from golftracker import golf_swing_repository
from golftracker import video_utils
from golftracker import image_operation
from golftracker import club_detection
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
    print(f">>Video file is {gs.video_fname}")
    (video_frames, _) = video_utils.split_video_to_frames(gs.video_fname)

    mp_frames = gs.to_frames()

    #cv2.namedWindow("LabelPoses")
    print(f"Found {len(mp_frames)} frames with starting pose")
    canny = image_operation.CannyEdgeDetection()
    line_detector = image_operation.LineDetector()

    if len(mp_frames) > 0:
        idx = 0
        key_pressed = ''

        print(f">> Press 'q' to save to csv OR Esc to return")
        while key_pressed != ord('q') and key_pressed != 27: # Esc key

            if key_pressed == ord('p'):
                # Previous frame
                idx -= 1
                

            if key_pressed == ord('n') or key_pressed == 32:
                # Next frame
                idx += 1

            # Sanitize
            if(idx < 0) :
                idx = 0
            if (idx >= len(mp_frames)):
                idx = len(mp_frames) -1

                
            canny_img = canny.process(video_frames[idx])
            single_channel_canny_edges = cv2.cvtColor(canny_img, cv2.COLOR_BGR2GRAY)
            lines = line_detector.process(single_channel_canny_edges)
            points = gs.get_screen_points(idx)

            all_lines_img = line_detector.draw(single_channel_canny_edges)
            club_lines = club_detection.detect_club_lines(lines, points)

            line_img = copy.deepcopy(mp_frames[idx]) #np.zeros(img.shape, dtype=np.uint8)
            line_img = cv2.circle(line_img, points["right_wrist"], radius=10, color=(0,255, 128), thickness=-1)
            line_img = cv2.circle(line_img, points["right_elbow"], radius=10, color=(128,255, 128), thickness=-1)

            for club_line in club_lines[0:1]:
                print(f"ClubLine={club_line}")
                x1, y1, x2, y2 = club_line
                line_img = cv2.line(line_img, (x1, y1), (x2, y2), color=(255, 128, 128), thickness=3) 
                
            stacked_images = video_utils.stack_images(([video_frames[idx], mp_frames[idx]], 
                                                       [all_lines_img, line_img]), scale=0.6,
                                                       labels=([f"Frame{idx}", "MediaPipe"],
                                                               ["AllLines", f"{gs.get_golf_pose(idx)}"]))
            cv2.imshow("StackedImages", stacked_images)
            key_pressed = cv2.waitKey(-1) & 0xff
    
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
