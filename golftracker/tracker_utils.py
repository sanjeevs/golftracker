# Utility for various tracker algorithms
import os
import cv2
import json
from pathlib import Path


def trackers_to_json_str(trackers):
    """Return a json str for the trackers."""

    return json.dumps(trackers)


def trackers_to_json(json_fnames, trackers_lst):
    """Write the trackers to json files."""

    for idx, f in enumerate(json_fnames):
        with open(f, "w") as fh:
            fh.write(trackers_to_json_str(trackers_lst[idx]))

def draw_trackers_on_frame(frame, trackers):
    h, w, c = frame.shape
    for t in trackers.keys():
        x = int(trackers[t].x * w)
        y = int(trackers[t].y * h)
        cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0), thickness=-1)