"""
ChatGPT inspired code.
"""
import os

test_mp4 = os.path.join("..", "assets", "test1.mov")

import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture(test_mp4)

# Define region of interest (ROI) around the golf club head
x, y, w, h = 320, 555, 20, 20

# Set up parameters for Farneback optical flow algorithm
params = dict(pyr_scale=0.5, levels=3, winsize=15, iterations=3, poly_n=5, poly_sigma=1.2, flags=0)

# Initialize previous frame and previous points for optical flow
prev_frame = None
prev_pts = None

while True:
    # Read current frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Select ROI around golf club head
    roi = gray[y:y+h, x:x+w]
    
    # Resize ROI for better optical flow performance
    roi_small = cv2.resize(roi, (0,0), fx=0.5, fy=0.5)
    
    # Compute optical flow using Farneback algorithm
    if prev_frame is not None and prev_pts is not None:
        flow = cv2.calcOpticalFlowFarneback(prev_frame, roi_small, None, **params)
        
        # Compute average flow magnitude and direction within ROI
        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        avg_mag = np.mean(mag)
        avg_ang = np.mean(ang)
        
        # Draw arrow to show direction of flow
        pt1 = (int(x+w/2), int(y+h/2))
        pt2 = (int(x+w/2+avg_mag*np.cos(avg_ang)), int(y+h/2+avg_mag*np.sin(avg_ang)))
        cv2.arrowedLine(frame, pt1, pt2, (0, 0, 255), thickness=2)
    
    # Update previous frame and previous points
    prev_frame = roi_small.copy()
    prev_pts = cv2.goodFeaturesToTrack(roi_small, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
    
    # Draw rectangle around ROI
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
    # Display frame
    cv2.imshow('Frame', frame)
    
    # Exit if 'q' key is pressed
    if cv2.waitKey() == ord('q'):
        break

# Release video capture and close window
cap.release()
cv2.destroyAllWindows()
