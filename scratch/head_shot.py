import os

test_img = os.path.join("..", "assets", "test1_frame0.jpg")
import cv2

# Read in the original frame
frame = cv2.imread(test_img)

# Define the coordinates of the nose position in the frame
nose_x = 200
nose_y = 320

# Define the size of the bounding box
bbox_size = 50

# Calculate the coordinates of the top-left and bottom-right corners of the bounding box
bbox_tl = (nose_x - bbox_size//2, nose_y - bbox_size//2)
bbox_br = (nose_x + bbox_size//2, nose_y + bbox_size//2)

# Crop the bounding box from the original frame
bbox = frame[bbox_tl[1]:bbox_br[1], bbox_tl[0]:bbox_br[0]]

# Resize the bounding box to the size of the original frame
bbox_resized = cv2.resize(bbox, (frame.shape[1], frame.shape[0]))

# Display the original frame and the enlarged bounding box
cv2.imshow('Original Frame', frame)
cv2.imshow('Enlarged Bounding Box', bbox_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
