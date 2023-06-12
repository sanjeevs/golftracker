'''
Track the path followed by various points in the video.
'''
import numpy as np
from golftracker import geom
from scipy.interpolate import interp1d

def get_path(gs, pt):
    norm_path = gs.get_norm_point_path(pt)
    scaled_path = geom.scale(norm_path, gs.width, gs.height)
    return scaled_path

def moving_average(positions, window_size):
    cumsum = np.cumsum(np.insert(positions, 0, 0, axis=0), axis=0)
    return (cumsum[window_size:] - cumsum[:-window_size]) / window_size

def cubic_spline_interpolation(positions, num_points):
    x = np.arange(len(positions))
    y = np.array(positions)

    # Create the interpolation functions for x and y coordinates
    fx = interp1d(x, y[:, 0], kind='cubic')
    fy = interp1d(x, y[:, 1], kind='cubic')

    # Generate new, equally spaced x-values
    x_new = np.linspace(0, len(positions) - 1, num_points)

    # Compute the smoothed positions
    smoothed_positions = np.column_stack((fx(x_new), fy(x_new)))
    int_positions = [(int(x), int(y)) for x, y in smoothed_positions]
    return int_positions

