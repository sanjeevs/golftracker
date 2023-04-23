import cv2
import numpy as np

# Create a named window to attach trackbars
cv2.namedWindow('image')

# Load image and convert to grayscale
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define default parameter values
thresh1 = 50
thresh2 = 150
apertureSize = 3
minLineLength = 50
maxLineGap = 10

# Define a function to update parameter values
def update(val):
    global thresh1, thresh2, apertureSize, minLineLength, maxLineGap
    thresh1 = cv2.getTrackbarPos('thresh1', 'image')
    thresh2 = cv2.getTrackbarPos('thresh2', 'image')
    apertureSize = cv2.getTrackbarPos('apertureSize', 'image')
    minLineLength = cv2.getTrackbarPos('minLineLength', 'image')
    maxLineGap = cv2.getTrackbarPos('maxLineGap', 'image')
    if apertureSize % 2 == 0:
        apertureSize += 1  # Make sure aperture size is odd
    if minLineLength <= 0:
        minLineLength = 1
    if maxLineGap < 0:
        maxLineGap = 0

# Create trackbars to vary parameters
cv2.createTrackbar('thresh1', 'image', thresh1, 255, update)
cv2.createTrackbar('thresh2', 'image', thresh2, 255, update)
cv2.createTrackbar('apertureSize', 'image', apertureSize, 7, update)
cv2.createTrackbar('minLineLength', 'image', minLineLength, 500, update)
cv2.createTrackbar('maxLineGap', 'image', maxLineGap, 500, update)

while True:
    # Apply Canny edge detection with current parameter values
    edges = cv2.Canny(gray, thresh1, thresh2, apertureSize)

    # Find lines in the image
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

    # Draw lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Display the image with current parameter values
    cv2.imshow('image', img)

    # Wait for key press and exit if 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release the video capture and close all windows
cv2.destroyAllWindows()
