#
# Root object.
#


import json


class GolfSwing:
    def __init__(self, height, width):
        self.frame_trackers = []
        self.height = height
        self.width = width

    def _out_format(self):
        fmt = {}
        fmt['height'] = self.height
        fmt['width'] = self.width
        frames_lst = []
        for idx in range(len(self.frame_trackers)):
            entry = {}
            entry["frame_idx"] = idx
            entry["frame_tracker"] = self.frame_trackers[idx]._points
            frames_lst.append(entry)
        fmt['frames'] = frames_lst
        return fmt

    def __str__(self):
        return str(self._out_format())

    def __repr__(self):
        return json.dumps(self._out_format())

    def to_json(self):
        return self.__repr__()

    def save_to_json(self, fname):
        with open(fname, "w") as fh:
            json.dump(self._out_format(), fh, indent=2)
