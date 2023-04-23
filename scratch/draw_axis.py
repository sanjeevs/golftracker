import cv2
import numpy as np

# create a black image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# set the origin point
origin = (200, 200)

# draw dashed x-axis
cv2.line(img, (0, origin[1]), (400, origin[1]), (255, 255, 255), 1, cv2.LINE_AA)
for x in range(0, 400, 20):
    cv2.line(img, (x, origin[1] - 5), (x, origin[1] + 5), (255, 255, 255), 1, cv2.LINE_AA)

# draw dashed y-axis
cv2.line(img, (origin[0], 0), (origin[0], 400), (255, 255, 255), 1, cv2.LINE_AA)
for y in range(0, 400, 20):
    cv2.line(img, (origin[0] - 5, y), (origin[0] + 5, y), (255, 255, 255), 1, cv2.LINE_AA)

# show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
