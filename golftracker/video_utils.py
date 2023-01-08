import cv2
import numpy as np

def transform_frame(frame, scale=100, rotate=""):

    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    if rotate == "90":
        out_frame = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
    elif rotate == "180":
        out_frame = cv2.rotate(resized, cv2.ROTATE_180)
    else:
        out_frame = resized
    return out_frame


def split_video_to_frames(video_fname, scale=100, rotate=0):
    """ Split a video file and return frames and other info."""

    frames = []
    cap = cv2.VideoCapture(video_fname)
    if not cap.isOpened():
        raise ValueError(f"Could not open file '{video_fname}'")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    while 1:
        flag, frame = cap.read()
        if not flag:
            break
        else:
            # Video frames seem to be in correct RGB format. So no conversion needed
            # rgb_frame = frame #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out_frame = transform_frame(frame, scale, rotate)
            frames.append(out_frame)
          
    (height, width, _) = frames[0].shape

    # Paranoia check.
    assert frames[0].dtype == 'uint8'
    print(f">>New video has width={width}, ht={height}, fps={fps}")
    cap.release()

    return (frames, (width, height, fps))


def join_frames_to_video(video_fname, fps, frames):
    if len(frames) == 0:
        raise ValueError("Must specify at least 1 frame to be written")

    init_frame = frames[0]
    if init_frame is None:
        raise ValueError(f"Could not load init frame")

    height, width, _ = init_frame.shape

    video = cv2.VideoWriter(
        video_fname, cv2.VideoWriter.fourcc(*"mp4v"), fps, (width, height)
    )

    for frame in frames:
        video.write(frame)
    video.release()

    return len(frames)


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
        blank_frame = np.zeros((height, width, 3), np.uint8)
        frames.append(blank_frame)
    return frames


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
        print("colsAvailable")
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(labels) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(labels[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,labels[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver
