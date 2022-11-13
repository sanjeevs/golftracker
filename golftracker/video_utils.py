import cv2
import numpy as np


def split_video_to_frames(video_fname):
    """ Split a video file into frames. """

    frames = []
    cap = cv2.VideoCapture(video_fname)
    if not cap.isOpened():
        raise ValueError(f"Could not open file '{video_fname}'")
    while(1):
        if cap.grab():
            flag, frame = cap.retrieve()
            if not flag:
                break
            else:
                frames.append(frame)
        else:
            break

    return frames


def join_frames_to_video(video_fname, fps, frames):
    if len(frames) == 0:
        raise ValueError("Must specify at least 1 frame to be written")

    init_frame = frames[0]
    if init_frame is None:
        raise ValueError(f"Could not load init frame")

    height, width, _ = init_frame.shape

    video = cv2.VideoWriter(
        video_fname, cv2.VideoWriter.fourcc(*"mp4v"), fps, (width, height))

    for frame in frames:
        video.write(frame)
    video.release()

    return len(frames)

def create_blank_frames(num_frames, height=100, width=200):
    """ 
    Utility to return a list of blank frames. 

    >>> create_blank_frames(0)
    []

    >>> len(create_blank_frames(3))
    3

    """
    frames = []
    for _ in range(num_frames):
        blank_frame = np.zeros((height, width, 3), np.uint8)
        frames.append(blank_frame)
    return frames