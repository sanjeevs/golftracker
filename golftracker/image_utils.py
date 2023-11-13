import cv2
import numpy as np
import copy

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

def stack_images(imgArray, scale, labels=[]):
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
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
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
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(labels) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(labels[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,labels[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
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
    elif isinstance(norm_points, list):
        return [scale_norm_point(v, width, height) for v in norm_points]
    elif isinstance(norm_points, (tuple, list)) and len(norm_points) == 2:
        return scale_norm_point(norm_points, width, height)
    else:
        raise TypeError("Unsupported input type for normalized points")
