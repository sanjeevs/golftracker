'''
Tune the cv2 parameters to detect line edges in a frame.
'''

import cv2
import argparse
import sys
import math
import numpy as np
import copy

from golftracker import golf_swing_repository
from golftracker import video_utils
from golftracker import image_utils
from golftracker import geom
from golftracker import image_operations as image_op
from golftracker import gt_const

from golftracker import canny_edge_detector
from golftracker import canny_edge_params

from golftracker import hough_line_detector
from golftracker import hough_line_params
from golftracker import image_operations as image_op

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Tune cv2 parameters to track the club head."
    )
    parser.add_argument(
        "-s", "--scale", type=int, default=60, help="Scale percent in output image",
    )
    parser.add_argument(
        "-i", "--idx", type=int, default=0, help="Frame to work on",
    )
    parser.add_argument("swing_db", type=str, help="Input golf swing data base")

    return parser


opt = create_parser().parse_args()
frame_idx = opt.idx

gs = golf_swing_repository.reconstitute(opt.swing_db)
canny_edge_params = gs.canny_edge_params
hough_line_params = gs.hough_line_params

video_frames = gs.get_video_frames()
num_frames = len(video_frames)

thumb_points = gs.get_screen_point_path("right_thumb")
print(f">>Extracted {len(thumb_points)} thumb points")

thumb_velocities = geom.compute_velocities(thumb_points, gs.fps)

if frame_idx >= num_frames:
    print(f"ERROR: No frame idx {frame_idx} detected in {num_frames} frames")
    raise ValueError("Invalid video frame detected")

frame = video_frames[frame_idx]
width, height, _ = frame.shape

def draw_main():
    #lines = gs.run_frame_line_detection(frame_idx, frame)
    
    #image_op.draw_lines(line_frame, lines)

    canny_edge_det = canny_edge_detector.CannyEdgeDetector(canny_edge_params)
    canny_frame = canny_edge_det.process(frame)

    hough_line_det = hough_line_detector.HoughLineDetector(hough_line_params)
    lines = hough_line_det.process(canny_frame)
    lines = gs.filter_frame_lines(frame_idx, lines)
    line_frame = np.zeros((width, height, 3), np.uint8)
    mp_points = gs.get_screen_points(frame_idx)
    points_to_draw = ['right_thumb', 'right_elbow', 'right_shoulder', 'left_shoulder']
    for pt in points_to_draw:
        cv2.circle(line_frame, mp_points[pt], 10, (0, 0, 255), -1)
    pt1, pt2, pt3,  pt4 = [mp_points[pt] for pt in points_to_draw]
    cv2.line(line_frame, pt1, pt2, (255, 0, 0), 3)
    cv2.line(line_frame, pt2, pt3, (255, 0, 0), 3)
    cv2.line(line_frame, pt3, pt4, (255, 0, 0), 3)
    image_op.draw_lines(line_frame, lines)

    filter_frame = np.zeros((width, height, 3), np.uint8)
    #candidates = gs.filter_frame_lines(frame_idx, lines)
    #image_op.draw_lines(filter_frame, candidates)

    stacked_images = image_utils.stack_images(
        ([frame, frame], [canny_frame, line_frame]),
        scale=opt.scale / 100,
        labels=(
            [f"Frame{frame_idx}", f"{gs.get_golf_pose(frame_idx)}"],
            ["CannyFr", "HoughLines"],
        ),
    )
    cv2.imshow("Main", stacked_images)


def on_trackbar(val, trackbar_id):
    """ Setup callback on track bar change. """
    if trackbar_id == 1:
        canny_edge_params.bin_threshold = cv2.getTrackbarPos("bin_thresh", "CannyEdgeTrackbar")
    if trackbar_id == 2:
        canny_edge_params.bin_maxvalue = cv2.getTrackbarPos("bin_maxvalue", "CannyEdgeTrackbar")
    if trackbar_id == 3:
        canny_edge_params.canny_threshold1 = cv2.getTrackbarPos("threshold1", "CannyEdgeTrackbar")
    if trackbar_id == 4:
        canny_edge_params.canny_threshold2 = cv2.getTrackbarPos("threshold2", "CannyEdgeTrackbar")
    draw_main()

def on_hg_trackbar(val, trackbar_id):
    if trackbar_id == 1:
        hough_line_params.rho = cv2.getTrackbarPos("rho", "HoughLineTrackbar") / 10
    if trackbar_id == 2:
        hough_line_params.theta = cv2.getTrackbarPos("theta", "HoughLineTrackbar") / 10
    if trackbar_id == 3:
        hough_line_params.threshold = cv2.getTrackbarPos("threshold", "HoughLineTrackbar")
    if trackbar_id == 4:
        hough_line_params.max_line_gap = cv2.getTrackbarPos("max_gap", "HoughLineTrackbar")
    draw_main()

def save():
    gs.canny_edge_params = canny_edge_params
    gs.hough_line_params = hough_line_params
    print(f'CannyEdgeParams:{gs.canny_edge_params}')
    print(f"HoughLineParams:{gs.hough_line_params}")
    golf_swing_repository.serialize(opt.swing_db, gs)
    print(f">>SAVE the pkl filke '{opt.swing_db}'")
   

#
# Main code starts
#
draw_main()
cv2.namedWindow("CannyEdgeTrackbar")
cv2.createTrackbar("bin_thresh", "CannyEdgeTrackbar", canny_edge_params.bin_threshold, 255, 
                   lambda v: on_trackbar(v, 1))
cv2.createTrackbar("bin_maxvalue", "CannyEdgeTrackbar", canny_edge_params.bin_maxvalue, 255, 
                   lambda v: on_trackbar(v, 2))
cv2.createTrackbar("threshold1", "CannyEdgeTrackbar", canny_edge_params.canny_threshold1, 255, 
                   lambda v: on_trackbar(v, 3))
cv2.createTrackbar("threshold2", "CannyEdgeTrackbar", canny_edge_params.canny_threshold2, 255, 
                   lambda v: on_trackbar(v, 4))

cv2.namedWindow("HoughLineTrackbar")
diagonal = math.sqrt(width^2 + height^2)
cv2.createTrackbar("rho", "HoughLineTrackbar", int(hough_line_params.rho * 10), int(diagonal * 10), 
                   lambda v: on_hg_trackbar(v, 1))
cv2.setTrackbarMin("rho", "HoughLineTrackbar", 1)

cv2.createTrackbar("theta", "HoughLineTrackbar", int(hough_line_params.theta * 10), 31, 
                   lambda v: on_hg_trackbar(v, 2))
cv2.setTrackbarMax("theta", "HoughLineTrackbar", 31)

cv2.createTrackbar("threshold", "HoughLineTrackbar", hough_line_params.threshold, 10, 
                   lambda v: on_hg_trackbar(v, 3))

cv2.createTrackbar("max_gap", "HoughLineTrackbar", hough_line_params.max_line_gap, 100, 
                   lambda v: on_hg_trackbar(v, 4))
cv2.setTrackbarMin("max_gap", "HoughLineTrackbar", 1)

skip_save = 0
key_pressed = ''

while key_pressed != ord('q') and key_pressed != 27 and key_pressed != ord('s'):
    if key_pressed == ord('p'):
        # Previous frame
        frame_idx = max(frame_idx -1, 0)
                
    if key_pressed == ord('n') or key_pressed == 32:
        # Next frame
        frame_idx = min(frame_idx + 1, num_frames -1)

    key_pressed = cv2.waitKey(-1) & 0xff

    frame = video_frames[frame_idx]
    draw_main()

if key_pressed == ord("s"):
    save()
elif key_pressed == ord("q"):  
    ans = input(f">>> Do you want to update the pkl file '{opt.swing_db}'  (y/n) ")
    if ans == "yes" or ans == "y" or ans == "Y" or ans == "":
        save()

cv2.destroyAllWindows()
sys.exit(0)
