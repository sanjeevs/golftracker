#
# Media pipe service that processes the frames and returns landmarks


import mediapipe as mp

mp_pose = mp.solutions.pose
import cv2


def run(golf_swing, frames):
    """Run media pipe and update golf swing. """

    golf_swing.mp_pose_frame_landmarks = []

    for idx, frame in enumerate(frames):
        with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=1,
            enable_segmentation=True,
            min_detection_confidence=0.5,
        ) as pose:
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                landmark = results.pose_landmarks.landmark
                golf_swing.mp_pose_frame_landmarks.append(landmark)
            else:
                golf_swing.mp_pose_frame_landmarks.append([])