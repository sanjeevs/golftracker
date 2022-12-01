#
# Point geometry
#
import math


def gradient(pt1, pt2):
    """ Return the slope of the line. """
    return (pt2[1] - pt1[1])/(pt2[0] - pt1[0])


def acute_angle_degrees(pt1, pt2, pt3):
    # Get the acute angle between 2 lines
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    radians = math.atan((m2 - m1)/(1 + (m1*m2)))
    degrees = round(math.degrees(radians))
    return degrees

def length(pt1, pt2):
    return math.dist(pt1, pt2)