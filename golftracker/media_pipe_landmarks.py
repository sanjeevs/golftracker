"""
Results for media pipe processing
----------------------------------
This stores the results of mp processing as a flat row of 4 coordinates (x, y, z, v) per landmark.
"""

import numpy as np
import logging
from golftracker import gt_const as gt
from golftracker import media_pipe_operation as ml_op

class MediaPipeLandmarks:
    """
    Returns the (x,y) coordinates of the media pipe landmark in screen coordinates..
    """

    def __init__(self, num_frames):
        self.video_landmarks = [[]] * num_frames

    def set_mp_results(self, video_landmarks):
        self.video_landmarks = video_landmarks

    def get_mp_landmarks_flat_row(self, idx):
        frame_landmark = self.video_landmarks[idx]
        return gt.get_mp_landmarks_flat_row(frame_landmark)
      
    def get_screen_points(self, frame_idx, height, width):
        """ 
        Return the landmarks for a frame in screen coordinates.

        :param frame_idx: Frame index
        :param height: Height of the frame
        :param width: Width of the frame
        :rtype: dict
        :return: Dictionary of all the landmark coordinates.
        """
        data = {}
        i = 0
        row = self.get_mp_landmarks_flat_row(frame_idx)
        if row:
            for entry in gt.MP_POSE_LANDMARKS:
                data[entry] = [int(row[i] * width), int(row[i + 1] * height)]
                i += 4
        return data

    def draw_frame(self, frame_idx, background_frame):
        """
        Draw the media pipe landmarks on the background frames.
        """
        frame_landmarks = self.video_landmarks[frame_idx]
        ml_op.draw(background_frame, frame_landmarks)