""" Tracks the position of various elements in a golf swing."""

import json
from types import SimpleNamespace

class Tracker:
    def __init__(self):
        """Initialize the trackers with none values.

        :ivar ball: List of 2 values
        :ivar shaft: List of 4 values. Each pair is single coordinate value.
        """
        self.ball = [None] * 2
        self.shaft = [None] * 4

    def is_empty(self):
        """
        Check if the user has selected any tracker.

        :return: True if a tracker has non None value
        """
        if self.ball[0] == None and self.shaft[0] == None:
            return True
        else:
            return False

    def update_ball(self, x, y):
        """Store the position of the ball.

        :param x: screen x coordinate of the ball tracker.
        :param y: screen y coordinate of the ball tracker.
        """
        self.ball[0] = x
        self.ball[1] = y

    def update_shaft(self, x, y):
        """Store the pos of the shaft.

        :param x: screen x corodinate of the shaft tracker.
        :param y: screen y corordinate of the shaft tracker.
        """
        if self.shaft[0]:
            self.shaft[2] = x
            self.shaft[3] = y
        else:
            self.shaft[0] = x
            self.shaft[1] = y

    def to_json(self):
        """Returns json string repr. if all values are null then return empty string
        """
        if self.is_empty():
            return ""
        else:
            return json.dumps(self.__dict__)

    def merge_default(self, obj):
        if self.ball[0] == None:
            self.ball = obj.ball
        if self.shaft[0] == None:
            self.shaft[0] = obj.shaft[0]
            self.shaft[1] = obj.shaft[1]
        if self.shaft[2] == None:
            self.shaft[2] = obj.shaft[2]
            self.shaft[3] = obj.shaft[3]

def make_from_json(json_str):
    tmp = json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
    return tmp
