#
# Model the golf swing as a double pendlum
import cv2

def draw(img, points):
	h, w, _ = img.shape
	img = cv2.line(img, points["left_shoulder"], points["right_shoulder"], 
		           color=(255, 128, 128), thickness=3)

	x = int((points['left_shoulder'][0] + points['right_shoulder'][0]) / 2)
	y = int((points['left_shoulder'][1] + points['right_shoulder'][1]) / 2)
	pivot1 = (x, y)
	pivot2 = points['right_wrist']

	img = cv2.line(img, points["left_shoulder"], pivot2, 
		           color=(255, 128, 128), thickness=3)

	img = cv2.line(img, points["right_shoulder"], pivot2, 
		           color=(255, 128, 128), thickness=3)
	img = cv2.line(img, pivot1, pivot2, 
		           color=(255, 128, 128), thickness=3)

	img = cv2.line(img, pivot1, (pivot1[0], h), color=(0, 128, 128), thickness=2)
	return img