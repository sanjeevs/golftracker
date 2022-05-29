""" Tracks the position of various elements in a golf swing."""

import json


class Tracker:
    def __init__(self):
        self.ball = [None] * 2
        self.shaft = [None] * 4

    def update_ball(self, x, y):
        self.ball[0] = x
        self.ball[1] = y

    def update_shaft(self, x, y):
        """Store the pos of the shaft."""
        if self.shaft[0]:
            self.shaft[2] = x
            self.shaft[3] = y
        else:
            self.shaft[0] = x
            self.shaft[1] = y

    def to_json(self):
        """Returns json string representiation."""
        return json.dumps(self.__dict__)

