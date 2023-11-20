import cv2
import numpy as np
import copy
from collections.abc import Sequence

RGB_VALUES = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "light_gray": (211, 211, 211),
    "pale_blue": (173, 216, 230),    
}

BGR_VALUES = {color: (b, g, r) for color, (r, g, b) in RGB_VALUES.items()}


def create_blank_frames(num_frames, height=100, width=200):
    """ 
    Utility to return a list of blank frames. 

    >>> create_blank_frames(0)
    []

    >>> len(create_blank_frames(3))
    3

    """
    frames = []
    for _ in range(num_frames):
        frames.append(create_blank_frame(height, width))
    return frames


def create_blank_frame(height, width):
    blank_frame = np.zeros((height, width, 3), np.uint8)
    return blank_frame


def _clean_input_stack_images(images, n):
    '''
    Clean up input to stack_images.
    1. Must be even number of images.
    2. Each entry must have the frame and the label.
    '''
    if n <= 1:
        return images
    else:
        if n % 2 == 1:
            min_num_images = n + 1
        else:
            min_num_images = n

        out_images = []
        for i in range(min(len(images), n)):
            item = images[i]
            if not isinstance(item, Sequence):
                out_images.append([item, ""])
            else:
                out_images.append(item)
        left_len = min_num_images - len(out_images)
        if left_len > 0:
            for i in range(left_len):
                h, w, _ = images[0][0].shape
                out_images.append([create_blank_frame(h, w), "Blank"])
        return out_images, min_num_images


def stack_images(images, scale, num_windows):
    img_lst, n = _clean_input_stack_images(images, num_windows)
    img_2d, label_2d = [], []

    if n == 1:
        # Add first image and its label for one window
        img_2d.append([img_lst[0][0]])
        label_2d.append([img_lst[0][1]])
    else:
        # Handle cases for two or more windows
        for i in range(0, n, 2):
            img_2d.append([img_lst[i][0], img_lst[i+1][0]])
            label_2d.append([img_lst[i][1], img_lst[i+1][1]])

    return stack_2d_images(imgArray=img_2d, scale=scale, labels=label_2d)

def stack_2d_images(imgArray, scale, labels=[]):
    """ Helper routine copied from web.
        https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects/blob/master/Basics/Joining_Multiple_Images_To_Display.py
    """
    sizeW= int(imgArray[0][0].shape[1] * scale)
    sizeH = int(imgArray[0][0].shape[0] * scale)
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), 
                        None, scale, scale)
                if len(imgArray[x][y].shape) == 2: 
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), 
                    None, scale, scale)
            if len(imgArray[x].shape) == 2: 
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(labels) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver, (c*eachImgWidth,eachImgHeight*d),
                        (c*eachImgWidth+len(labels[d][c])*13+27,30+eachImgHeight*d),
                        (255,255,255),cv2.FILLED)
                cv2.putText(ver,labels[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),
                        cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver


def create_roi(point, width, height):
    '''
    Calculate the coordinates of the top-left and bottom-right corners of the rectangle.
    '''
    x1 = point[0] - width // 2
    y1 = point[1] - height // 2
    x2 = point[0] + width // 2
    y2 = point[1] + height // 2

    return (x1, y1), (x2, y2)

def create_right_triangle(img, pt1, pt2):
    # Compute the third point of the triangle
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]
    pt3 = [pt1[0] + dy, pt1[1] - dx]

    # Draw the triangle
    pts = np.array([pt1, pt2, pt3], np.int32)
    return pts

def draw_triangle(img, pt1, pt2, pt3, color, thickness):
    # Draw the three lines that form the triangle
    cv2.line(img, pt1, pt2, color, thickness)
    cv2.line(img, pt2, pt3, color, thickness)
    cv2.line(img, pt3, pt1, color, thickness)

def scale_norm_point(pt, width, height):
    return (int(pt[0] * width), int(pt[1] * height))

def norm_2_screen(norm_points, width, height):
    '''
    Convert the normalized points to screen points.
    Can handle dict, list or a scalar value.
    '''
    if isinstance(norm_points, dict):
        return {k: scale_norm_point(v, width, height) for k, v in norm_points.items()}
    elif isinstance(norm_points, (tuple, list)):
        result = []
        for i, v in enumerate(norm_points):
            if isinstance(v, (int, float)):
                if i % 2 == 0:
                    result.append(int(v * width))
                else:
                    result.append(int(v * height))
            else:
                result.append(scale_norm_point(v, width, height))
        return result
    else:
        raise TypeError("Unsupported input type for normalized points")
