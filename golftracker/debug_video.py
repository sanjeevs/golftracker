import argparse
import cv2
import numpy as np


def stackImages(scale,imgArray):
    """ Helper routine copied from web. """

    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Merge the default values to json file(s)"
    )

    parser.add_argument(
        "in_video", type=str, help="Input video file name"
    )

    parser.add_argument(
        "out_video", type=str, help="Ouput video file name"
    )

    parser.add_argument(
        "--scale",
        "-s",
        default=100,
        type=int,
        help="resize the incoming video file by scale percent"
    )

    parser.add_argument(
        "--rotate",
        "-r",
        default="",
        help="rotate the incoming video file",
    )

    return parser


def main():
	opt = create_parser().parse_args()
	in_cap = cv2.VideoCapture(opt.in_video)
	if not in_cap.isOpened():
		raise ValueError(f"Could not open in video {opt.in_video}")

	out_cap = cv2.VideoCapture(opt.out_video)
	if not out_cap.isOpened():
		raise ValueError(f"Could not open out video {opt.out_video}")

	frame_cnt = 1
	while(in_cap.isOpened()):
		ret, in_frame = in_cap.read()

		if ret:
			if opt.rotate == "90":
				in_frame = cv2.rotate(in_frame, cv2.ROTATE_90_CLOCKWISE)
			elif opt.rotate == "180":
				in_frame = cv2.rotate(in_frame, cv2.ROTATE_180)

			flag, out_frame = out_cap.read()
			cv2.putText(out_frame, f"Frame:{frame_cnt}", (50, 50), 
						cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
			if not flag:
				raise ValueError(f"Error reading from from out video")

			img_stack = stackImages(opt.scale/100, ([in_frame, out_frame]))
			cv2.imshow("Stack", img_stack)
			key_pressed = cv2.waitKey(0) & 0xff
			if key_pressed == ord('q'):
				break
			frame_cnt += 1
		else:
			break

	in_cap.release()
	out_cap.release()

	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
