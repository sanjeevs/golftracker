# Script
# Convert a video into a media pipe stick figure video

import argparse
import cv2


from golftracker import video_utils
from golftracker import golf_swing as gs
from golftracker import draw_operation as draw_op
from golftracker import media_pipe_operation as mp_op


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Merge the default values to json file(s)"
    )

    parser.add_argument(
        "in_video", type=str, help="Input video file name"
    )

    parser.add_argument(
        "out_video", type=str, help="Ouput video file name"
    )

    parser.add_argument(
        "--scale",
        "-s",
        default=100,
        type=int,
        help="resize the incoming video file by scale percent"
    )

    parser.add_argument(
        "--fps",
        "-f",
        default=20,
        type=int,
        help="Frames per second of out video"
    )

    parser.add_argument(
        "--rotate",
        "-r",
        default="",
        help="rotate the incoming video file",
    )

    return parser

def transform_frame(opt, frame):
    if opt.rotate == "90":
        out_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif opt.rotate == "180":
        out_frame = cv2.rotate(frame, cv2.ROTATE_180)
    else:
        out_frame = frame

    return out_frame

def display_result_images(opt):
    in_cap = cv2.VideoCapture(opt.in_video)
    if not in_cap.isOpened():
        raise ValueError(f"Could not open in video {opt.in_video}")

    out_cap = cv2.VideoCapture(opt.out_video)
    if not out_cap.isOpened():
        raise ValueError(f"Could not open out video {opt.out_video}")

    frame_cnt = 1
    while(in_cap.isOpened()):
        ret, in_frame = in_cap.read() 

        if ret:
            t_in_frame = transform_frame(opt, in_frame)

            ret, out_frame = out_cap.read()
            if not ret:
                    raise ValueError(f"Error reading from from out video")
            t_out_frame = transform_frame(opt, out_frame)
            
            cv2.putText(t_out_frame, f"Frame:{frame_cnt}", (50, 50), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

            img_stack = video_utils.stack_images(opt.scale/100, ([t_in_frame, t_out_frame]))
            cv2.imshow("Stack", img_stack)
            key_pressed = cv2.waitKey(0) & 0xff
            if key_pressed == ord('q'):
                break
            frame_cnt += 1
        else:
            break

    in_cap.release()
    out_cap.release()

    cv2.destroyAllWindows()


def main():
    opt = create_parser().parse_args()
  
    frames = video_utils.split_fname_to_frames(opt.in_video)
    (height, width, _) = frames[0].shape

    golf_swing = gs.GolfSwing(frames)

    mp_op.run(frames, golf_swing.frame_contexts)
    stick_frames = draw_op.run(height, width, golf_swing.frame_contexts)

    video_utils.join_frames_to_fname(opt.out_video, fps=20, frames=stick_frames)

    display_result_images(opt)

if __name__ == "__main__":
    main()
