import cv2
import numpy as np


def stack_images(scale,imgArray):
    """ Helper routine copied from web. """

    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def split_fname_to_frames(video_fname):
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


def join_frames_to_fname(video_fname, fps, frames):
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