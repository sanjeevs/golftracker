import os
test_mp4 = os.path.join("..", "assets", "test1.mov")

import cv2

def detect_backswing(video_path, threshold=20):
    # Initialize VideoCapture object
    cap = cv2.VideoCapture(video_path)

    # Check if VideoCapture object was successfully initialized
    if not cap.isOpened():
        print("Could not open video file")
        return

    # Read first frame from video
    ret, frame = cap.read()

    # Prompt user to select initial position of golf club head
    x, y, w, h = cv2.selectROI("Select ROI", frame, False)

    # Initialize previous frame and previous bounding box
    prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prev_box = (x, y, w, h)

    # Loop through video frames
    while True:
        # Read current frame from video
        ret, frame = cap.read()

        # Check if frame was successfully read
        if not ret:
            break

        # Convert frame to grayscale
        curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate optical flow using Farneback algorithm
        flow = cv2.calcOpticalFlowFarneback(prev_frame, curr_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Calculate average displacement of golf club head over bounding box
        x_displacements = flow[y:y+h, x:x+w, 0]
        y_displacements = flow[y:y+h, x:x+w, 1]
        avg_x_displacement = sum(x_displacements.flatten()) / x_displacements.size
        avg_y_displacement = sum(y_displacements.flatten()) / y_displacements.size

        # Check if backswing has been detected
        if abs(avg_x_displacement) > threshold:
            # Draw red bounding box around golf club head
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Display frame with bounding box
        cv2.imshow("Frame", frame)

        # Update previous frame and bounding box
        prev_frame = curr_frame
        prev_box = (x, y, w, h)

        # Wait for key press or exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # Release VideoCapture object and destroy windows
    cap.release()
    cv2.destroyAllWindows()

detect_backswing(test_mp4 )