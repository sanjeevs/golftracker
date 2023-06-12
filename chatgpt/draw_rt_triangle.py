import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Define the vertices of the triangle
pt1 = (100, 100)
pt2 = (200, 200)
pt3 = (100, 200)

# Draw the triangle
cv2.line(img, pt1, pt2, (255, 255, 255), 2)
cv2.line(img, pt2, pt3, (255, 255, 255), 2)
cv2.line(img, pt3, pt1, (255, 255, 255), 2)

# Find the length of the two sides of the triangle
a = np.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
b = np.sqrt((pt3[0] - pt2[0])**2 + (pt3[1] - pt2[1])**2)

# Find the angle between the two sides of the triangle
theta = np.arctan2(pt2[1] - pt1[1], pt2[0] - pt1[0]) - np.arctan2(pt3[1] - pt2[1], pt3[0] - pt2[0])
theta = np.degrees(theta)
if theta < 0:
    theta += 180

# Find the coordinates of the point where the two sides meet
x = pt2[0] + int(b*np.cos(np.radians(theta)))
y = pt2[1] + int(b*np.sin(np.radians(theta)))

# Draw the third side of the triangle
cv2.line(img, pt1, (x, y), (255, 255, 255), 2)

# Show the image
cv2.imshow('Right Angle Triangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
