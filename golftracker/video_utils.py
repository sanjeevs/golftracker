import cv2
import os

from pathlib import Path
from golftracker import file_utils


class VideoSplitter:
    """ Helper class to split a video file into frames."""

    def __init__(self, fname):
        """Construct a video object.
        :raises : Value error if the file is not found.
        """
        self.cap = cv2.VideoCapture(fname)
        if not self.cap.isOpened():
            raise ValueError(f"Could not open {fname}")

    def __iter__(self):
        return self

    def __next__(self):
        if self.cap.grab():
            flag, frame = self.cap.retrieve()
            if not flag:
                raise StopIteration
            else:
                return frame
        else:
            raise StopIteration

    def __del__(self):
        self.cap.release()

    def num_frames(self):
        """Return the number of frames in the video file."""
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

def split_video_to_frames(video_fname, framedir=""):
    """
        Split the video into frames and store in framedir
        Returns the number of frames created.
    """

    if framedir == "":
        framedir = Path(video_fname).stem

    file_utils.create_framedir(framedir, empty=1)
    video_frames = VideoSplitter(video_fname)
    frame_fnames = file_utils.create_frame_fnames(video_frames.num_frames())

    for idx, frame in enumerate(video_frames):
        cv2.imwrite(os.path.join(framedir, frame_fnames[idx]), frame)

    return video_frames.num_frames()

def join_frames_to_video(video_fname, fps, framedir, fname_exp):
    """
    Join all the frames that match the frame file name expression into a video file.
    Return the number of frames in the output video

    """
    frame_fnames = file_utils.select_frame_fnames_from_dir(framedir, fname_exp)
    if len(frame_fnames) == 0:
        raise ValueError(f"No frame file selected in '{framedir}' with '{fname_exp}'")

    init_frame = cv2.imread(frame_fnames[0])
    if init_frame is None:
        raise ValueError(f"Could not load frame {frame_fnames[0]}")

    height, width, _ = init_frame.shape

    video = cv2.VideoWriter(
        video_fname, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )

    for fname in frame_fnames:
        frame = cv2.imread(fname)
        video.write(frame)
    video.release()

    return len(frame_fnames)