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

    def set_video_landmarks(self, video_landmarks):
        '''
        Store the result of the media pipe operation.
        Each landmark is a tuple of 4 values (x, y, z, visibility)
        '''
        self.video_landmarks = video_landmarks

    def get_mp_landmarks_flat_row(self, frame_idx):
        frame_landmarks = self.video_landmarks[frame_idx]
        return gt.get_mp_landmarks_flat_row(frame_landmarks)
    
    def get_norm_points_dict(self, frame_idx):
        """ 
        Return the landmarks for a frame in norm screen coordinates.

        :param frame_idx: Frame index
        :rtype: dict
        :return: Dictionary of all the landmark coordinates.
                 Key is defined in const MP_POSE_LANDMARKS.
        """
        data = {}
        i = 0
        row = self.get_mp_landmarks_flat_row(frame_idx)
        if row:
            for entry in gt.MP_POSE_LANDMARKS:
                data[entry] = [row[i], row[i + 1]]
                i += 4 #(x, y, z, v)
        return data

    def get_norm_point(self, frame_idx, pt_name):

        row = self.get_mp_landmarks_flat_row(frame_idx)
        if not row:
            raise ValueError(f"Could not find mp row in frame_idx={frame_idx}")
        i = gt.MP_POSE_LANDMARKS.index(pt_name)
        return [row[i*4], row[i*4+1]]  #(x, y, z, v)
    
    def draw_frame(self, frame_idx, background_frame, line_color):
        """
        Draw the media pipe landmarks on the background frames.
        """
        frame_landmarks = self.video_landmarks[frame_idx]
        ml_op.draw(background_frame, frame_landmarks, line_color)


    def serialize(self):
        fmt = {}
        fmt['landmarks'] = gt.MP_POSE_LANDMARKS
        fmt['norm_points'] = []
        for frame_idx in range(len(self.video_landmarks)):
            fmt['norm_points'].append(self.get_mp_landmarks_flat_row(frame_idx))
        return fmt