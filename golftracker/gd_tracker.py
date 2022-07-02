""" Tracker for golf related parameters. """
from collections import namedtuple

ClubGrip = namedtuple("ClubGrip", "x y")


def add_club_grip(trackers, x, y):
    """Add club grip to the hash with normalized coordinates."""
    club_grip = ClubGrip(x, y)
    if club_grip in trackers.keys():
        raise ValueError("Duplicate value of club grib tracker")
    trackers["club_grip"] = club_grip


ClubToe = namedtuple("ClubToe", "x y")


def add_club_toe(trackers, x, y):
    """Add club toe to the hash with normalized coordinates."""
    club_toe = ClubToe(x, y)
    if club_toe in trackers.keys():
        raise ValueError("Duplicate value of club toe tracker")
    trackers["club_toe"] = club_toe


ClubHeel = namedtuple("ClubHeel", "x y")


def add_club_heel(trackers, x, y):
    """Add club heel to the hash with normalized coordinates."""
    club_heel = ClubHeel(x, y)
    if club_heel in trackers.keys():
        raise ValueError("Duplicate value of club heel tracker")
    trackers["club_heel"] = club_heel

GolfBall = namedtuple("GolfBall", "x y")


def add_golf_ball(trackers, x, y):
    """Add golf ball to the hash with normalized coordinates."""
    golf_ball = GolfBall(x, y)
    if golf_ball in trackers.keys():
        raise ValueError("Duplicate value of golf ball tracker")
    trackers["golf_ball"] = golf_ball
