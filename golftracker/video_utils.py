import cv2
import numpy as np

def transform_frame(frame, scale=100, rotate=""):

    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    if rotate == "90":
        out_frame = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
    elif rotate == "180":
        out_frame = cv2.rotate(resized, cv2.ROTATE_180)
    else:
        out_frame = resized
    return out_frame


def split_video_to_frames(video_fname, scale=100, rotate=0):
    """ Split a video file and return frames and other info."""

    frames = []
    cap = cv2.VideoCapture(video_fname)
    if not cap.isOpened():
        raise ValueError(f"Could not open file '{video_fname}'")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    while 1:
        flag, frame = cap.read()
        if not flag:
            break
        else:
            # Video frames seem to be in correct RGB format. So no conversion needed
            # rgb_frame = frame #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out_frame = transform_frame(frame, scale, rotate)
            frames.append(out_frame)
          
    (height, width, _) = frames[0].shape

    # Paranoia check.
    assert frames[0].dtype == 'uint8'
    print(f">>New video has width={width}, ht={height}, fps={fps}")
    cap.release()

    return (frames, (width, height, fps))


def join_frames_to_video(video_fname, fps, frames):
    if len(frames) == 0:
        raise ValueError("Must specify at least 1 frame to be written")

    init_frame = frames[0]
    if init_frame is None:
        raise ValueError(f"Could not load init frame")

    height, width, _ = init_frame.shape

    video = cv2.VideoWriter(
        video_fname, cv2.VideoWriter.fourcc(*"mp4v"), fps, (width, height)
    )

    for frame in frames:
        video.write(frame)
    video.release()

    return len(frames)


