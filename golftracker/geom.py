'''
Geometry algorithms.
'''

import math

def gradient(pt1, pt2):
    """ Return the slope of the line. """
    if pt2[0] == pt1[0]:
        # Instead of infinity return a large value
        return 100
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

def filter_lines_far_from_point(lines, point, max_dist):
    """Return a list of lines that are no further than max_dist from point."""
    result = []
    for line in lines:
        dist = shortest_dist_from_point_to_line(point, line)
        if dist < max_dist:
            result.append(line)
    return result

def filter_lines_with_wrong_slope(lines, slope, max_diff):
    """Return a list of lines that are too different in slope."""
    result = []
    for line in lines:
        s1 = slope_of_line(line)
        if (s1 * slope) > 0:  # Same sign
            if (abs(s1 - slope)) < max_diff:
                result.append(line)
    return result


def sort_lines_closest_to_point(lines, point, max_dist=50):
    """Sort the incoming lines in descending probability of being a club."""
    if lines == []:
        return []

    dist_lst = list(
        map(lambda l: shortest_dist_from_point_to_line(point, l), lines)
    )
    decorated_lst = list(zip(lines, dist_lst))
    decorated_lst.sort(key=lambda l: l[1])

    sorted_lines = [decorated_lst[i][0] for i in range(len(decorated_lst))]

    result = []
    for line in sorted_lines:
        dist = shortest_dist_from_point_to_line(point, line)
        if dist < max_dist:
            result.append(line)
        else:
            break

    return result


def sort_lines_matching_slope(lines, slope, max_diff=2):
    """Sort the incoming lines in descending probability of being a club."""
    if lines == []:
        return []

    slope_lst = list(map(lambda l: abs(slope_of_line(l) - slope), lines))
    decorated_lst = list(zip(lines, slope_lst))
    decorated_lst.sort(key=lambda l: l[1])

    sorted_lines = [decorated_lst[i][0] for i in range(len(decorated_lst))]

    result = []
    for line in sorted_lines:
        s1 = slope_of_line(line)
        if (s1 * slope) < 0:
            break
        if (abs(s1 - slope)) > max_diff:
            break
        result.append(line)

    return result

def segment_line(pt1, pt2, ntimes):
    """
    Return equidistant point on the line.

    >>> segment_line([0, 0], [100, 100], 0)
    []

    >>> segment_line([0,0], [100, 100], 1)
    [(50, 50)]

    >>> segment_line([0, 0], [100, 100], 2)
    [(33, 33), (66, 66)]
    """

    x_width = int((pt2[1] - pt1[1]) / (ntimes + 1))
    y_width = int((pt2[0] - pt1[0]) / (ntimes + 1))

    result = []
    for i in range(ntimes):
        x = pt1[0] + x_width * (i + 1)
        y = pt1[1] + y_width * (i + 1)
        result.append((x, y))

    return result

def compute_velocities(coords, fps):
    velocities = []
    for i in range(1, len(coords)):
        dx = coords[i][0] - coords[i-1][0]
        dy = coords[i][1] - coords[i-1][1]
        time_elapsed  = 1 / fps
        velocity = math.sqrt(dx**2 + dy**2) / time_elapsed 
        direction = math.atan2(dy, dx)
        sign = 1 if direction > 0 else -1
        velocities.append(sign * velocity)
    return velocities