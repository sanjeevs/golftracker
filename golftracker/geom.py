#
# Point geometry
#
import math


def gradient(pt1, pt2):
    """ Return the slope of the line. """
    if pt2[0] == pt1[0]:
        return 0
    else:
        return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])


def acute_angle_degrees(pt1, pt2, pt3):
    # Get the acute angle between 2 lines
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    radians = math.atan((m2 - m1) / (1 + (m1 * m2)))
    degrees = round(math.degrees(radians))
    return degrees

def length(pt1, pt2):
    return math.dist(pt1, pt2)

def line_equation_y(line):
    """ Return a lambda function that returns the y coordinate on the line at x pos.

    >>> line_equation_y([1, 2, 3, 4])(1)
    2.0
    
    """
    x1, y1, x2, y2 = line
    if x2 == x1:
        f = lambda x : y1
    else:
        m = (y2 - y1) / (x2 - x1)
        f  = lambda x : y1 + m * (x - x1)
    return f

def slope_of_line(line):
    """ Return the slope of line.

    >>> slope_of_line([0, 0, 100, 100])
    1.0

    """
    return gradient((line[0], line[1]), (line[2], line[3]))


def y_intercept_of_line(line):
    """ Return the y intercept of line.

    >>> y_intercept_of_line([0, 10, 100, 100])
    10.0

    """
    m = slope_of_line(line)
    b = line[1] - m * line[0]
    return b


def shortest_dist_from_point_to_line(point, line):
    """ Return the prependicular distance between point and line.

    >>> shortest_dist_from_point_to_line([5, 5], [0, 0, 100, 100])
    0.0

    >>> round(shortest_dist_from_point_to_line([5, 6], [0, -4/3, 2, 0]), 1)
    3.3

    """
    [x1, y1, x2, y2] = line
    slope = slope_of_line(line)
    y_intercept = y_intercept_of_line(line)
    dist = abs((slope * point[0]) - point[1] + y_intercept)/math.sqrt((slope * slope) + 1)
    return dist