""" 
Run the pose pipeline on a video file to create a new mp pose video.
"""
import argparse

import file_utils
import video_utils
import frame_tracker
import pose_detection
import visualize
import numpy as np
import cv2


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Merge the default values to json file(s)"
    )

    parser.add_argument(
        "in_video", type=str, help="Input video file name"
    )

    parser.add_argument(
        "--fps",
        "-f",
        default=10,
        type=int,
        help="Frame per second of output video",
    )

    parser.add_argument(
        "--out_video",
        "-o",
        default="mp.mp4",
        help="Null output video produced",
    )
    
    parser.add_argument(
        "--framedir",
        "-d",
        default="",
        help="output temp dir to store all the frames.",
    )
    return parser

def mp_process(in_frames):
    json_fnames = file_utils.frame_fnames_to_json_fnames(in_frames, suffix="_mp")

    frame_trackers = [frame_tracker.FrameTracker() for i in range(len(in_frames))]

    print(f">>Faking process by creating {len(json_fnames)} trackers json file")
    for idx, js in enumerate(json_fnames):
        frame_trackers[idx].to_json(json_fnames[idx])

    return json_fnames

def mp_visualize(json_fnames):
    out_fnames = file_utils.json_fnames_to_frame_fnames(json_fnames, prefix="__")

    # Create empty output frames. This would be the visualize steps
    for idx, f in enumerate(json_fnames):
        ft = frame_tracker.FrameTracker()
        ft.fm_json(f)
        blank_img = np.zeros((500, 500, 3), dtype="uint8")
        visualize.draw_frame_tracker(blank_img, ft)
        cv2.imwrite(out_fnames[idx], blank_img)

    return out_fnames


def main():
    opt = create_parser().parse_args()

    if opt.framedir == "":
        opt.framedir = file_utils.create_framedir_name(opt.in_video)

    file_utils.create_framedir(opt.framedir)
   
    print(f">>Splitting '{opt.in_video}'' into dir '{opt.framedir}' as frames in png format")

    in_frames = video_utils.split_video_to_frames(opt.in_video, opt.framedir)
    print(f">>Created {len(in_frames)} frames from video file '{opt.in_video}'")

    print(f">>Creating output mp video {opt.out_video}")
    video_utils.join_frames_to_video(opt.out_video, opt.fps, 
                                     mp_visualize(pose_detection.mp_process(in_frames)))


if __name__ == "__main__":
	main()