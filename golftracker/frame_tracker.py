# Immutable value object
# Frame tracker is an associative array of points that are tracked in each frame.

class FrameTracker:
    Pts = [
            "nose", 
            "left_eye", "right_eye", 
            "left_ear", "right_ear",
            "left_shoulder", "right_shoulder",
            "left_elbow", "right_elbow",
            "left_wrist", "right_wrist",
            "left_hip", "right_hip",
            "left_knee", "right_knee",
            "left_ankle", "right_ankle",
            "left_heel", "right_heel",
            "club_grip", "club_heel", "club_toe"
        ]

    def __init__(self, values={}):
        
        self._points = {}
        # Initialize all the trackers with default 0, 0 coord
        if not set(values.keys()).issubset(set(FrameTracker.Pts)):
            raise ValueError(f"Found invalid key in tracker init.")

        for t in FrameTracker.Pts:
            if t in values.keys():
                self._points[t] = values[t]
            else:
                self._points[t] = (0.0, 0.0)

        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(FrameTracker.Pts):
            self._index = -1
            raise StopIteration
        else:
            key = FrameTracker.Pts[self._index]
            return (key, self._points[key])

    def __len__(self):
        return len(FrameTracker.Pts)

    def is_null(self, key):
        return self._points[key] == (0, 0)

    def __getitem__(self, key):
        if key not in FrameTracker.Pts:
            raise ValueError(f"Invalid tracker name '{key}'")
        return self._points[key]

    def __eq__(self, other):
        """Equality for value object."""
        for t in FrameTracker.Pts:
            if other[t] != self[t]:
                return False
        return True

    def __hash__(self):
        h = 0
        for pt in self._points.values():
            h += (pt[0]  + pt[1]) * 100
        return int(h)

    def subsume(self, other):
        """ 
        Subsume means include or absorbs another. 
        Hence prefer the self value if not null, else other value.
        """
        rslt = {}
        for tracker in FrameTracker.Pts:
            if not self.is_null(tracker):
                rslt[tracker] = self[tracker]
            else:
                rslt[tracker] = other[tracker]

        return FrameTracker(rslt)

    def update(self, other):
        """ Update means prefer other non null values else self value. """
        rslt = {}
        for tracker in FrameTracker.Pts:
            if not other.is_null(tracker):
                rslt[tracker] = other[tracker]
            else:
                rslt[tracker] = self[tracker]

        return FrameTracker(rslt)