# Script
# Convert a video into a media pipe stick figure video

import argparse
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


from golftracker import video_utils
from golftracker import golf_swing_factory



def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Create a video of the json golf swing"
    )

    parser.add_argument(
        "json", type=str, help="Input golf swing json database"
    )

    parser.add_argument(
        "out_video", type=str, help="Ouput video file name"
    )

    parser.add_argument(
        "--fps",
        "-f",
        default=20,
        type=int,
        help="Frames per second of out video"
    )


    return parser

def main():
    opt = create_parser().parse_args()
    gs = golf_swing_factory.create_from_json(opt.json)

    print(f">>Creating a video of width={gs.width} x height={gs.height} at {opt.fps} fps")
    stick_frames = []
    for idx in range(gs.num_frames()):
        frame = np.zeros([gs.height, gs.width, 3], dtype=np.uint8)
        lst = gs.mp_pose_frame_landmarks[idx]
        
        x = 0
        landmark_lst = []
        while x < len(lst):
            n = landmark_pb2.NormalizedLandmark(x=lst[x], y=lst[x+1], z=lst[x+2], visibility=lst[x+3])
            landmark_lst.append(n)
            x += 4

        reconstructed = landmark_pb2.NormalizedLandmarkList(landmark=landmark_lst)
        
        mp_drawing.draw_landmarks(frame, reconstructed, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

        stick_frames.append(frame)
    
    video_utils.join_frames_to_video(opt.out_video, fps=opt.fps, frames=stick_frames)

if __name__ == "__main__":
    main()
