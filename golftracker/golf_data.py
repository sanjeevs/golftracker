import json
import numpy as np
from golftracker import gt_const as gt
import logging

class GolfData:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.mp_frame_landmarks = [[]] * num_frames
    
    # 
    # Query inteface
    #
    def get_mp_landmarks(self, frame_idx):
        return self.mp_frame_landmarks[frame_idx]

    def get_mp_landmarks_flat_row(self, frame_idx):
        """ Return media pipe landmarks as a list of tuple (x, y, z, v) normalized coordinates """
        log = logging.getLogger(__name__)
        rslt = self.get_mp_landmarks(frame_idx)
        if not rslt:
            log.info(f"Frame[{frame_idx}]:Not detected any landmarks. Returning null row.")
            row = gt.null_pose_row()
        else:
            row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in rslt.landmark]).flatten())
        return row

    
    # 
    # Command Interface
    # 
    def set_mp_landmarks(self, frame_idx, landmarks):
        self.mp_frame_landmarks[frame_idx] = landmarks

    
    
   