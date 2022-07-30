""" Traditional object tracking using open cv built in algorithms. """

import cv2


class ObjTracking:
    # OpenCV object tracker implementations
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.legacy.TrackerCSRT_create,
        "kcf": cv2.legacy.TrackerKCF_create,
        "boosting": cv2.legacy.TrackerBoosting_create,
        "mil": cv2.legacy.TrackerMIL_create,
        "tld": cv2.legacy.TrackerTLD_create,
        "medianflow": cv2.legacy.TrackerMedianFlow_create,
        "mosse": cv2.legacy.TrackerMOSSE_create
    }

    def __init__(self, algo="mil"):
        """Intialize with one of the supported algorithms."""

        if algo not in ObjTracking.OPENCV_OBJECT_TRACKERS:
            raise ValueError(f"Invalid value of tracker algo {algo}")
        self.algo = algo
        self.trackers = cv2.legacy.MultiTracker_create()

    def setup(self, frame, box):
        """
        Start the object tracking by providing the initial position of object.
        :param:frame: input frame
        :param:box: Bounding box of object to track [top_x, top_y, bot_x, bot_y]
        :returns:None
        """

        tracker = ObjTracking.OPENCV_OBJECT_TRACKERS[self.algo]()
        self.trackers.add(tracker, frame, box)

    def update(self, frame):
        """
        Run on each frame after the initial positon is given.
        :param:frame: frame to detect the object.
        :return:bbox: Bounding boxes (top_left_x, top_left_y, bot_right_x, bot_right_y) 
        """

        ok, boxes = self.trackers.update(frame)
        if ok:
            results = []
            for box in boxes:
                (x, y, w, h) = [int(v) for v in box]
                results.append((x, y, w, h))
            return results
        else:
            return []
