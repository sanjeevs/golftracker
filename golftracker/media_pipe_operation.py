"""
The `media_pipe_operation` service processes the frames and returns a list of landmarks for each frame.

"""

import mediapipe as mp
import logging
import cv2


def run(frames):
    """
    Run media pipe on the frames.

    :param frames: A list of video frames of the golf swing.
    :type frames: list
    :return: The list of pose landmarks for all frames. Each landmark is a list of [x, y, z, v].
    :rtype: List of lists of landmarks
    """
    log = logging.getLogger(__name__)
    log.info(f"Running media pipe on {len(frames)} frames")
    video_landmarks = []

    for frame_idx, frame in enumerate(frames):
        with mp.solutions.pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=True,
            min_detection_confidence=0.5
        ) as pose:
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                video_landmarks.append(results.pose_landmarks)
            else:
                video_landmarks.append([])
                log.info(f"Media pipe failed to find landmarks for frame_idx={frame_idx}")
    return video_landmarks


def draw(frame, frame_landmarks):
    """
    Draw the landmarks on the incoming frame.
    
    :param frame: The video frame to draw the landmarks on.
    :type frame: numpy.ndarray
    :param frame_landmarks: The pose landmarks to draw on the frame. Each landmark is a list of [x, y, z, v].
    :type frame_landmarks: list
    :return: None
    :rtype: None
    """
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    mp_drawing.draw_landmarks(
                frame,
                frame_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(
                    color=(245, 117, 66), thickness=2, circle_radius=2
                ),
                mp_drawing.DrawingSpec(
                    color=(245, 66, 230), thickness=2, circle_radius=2
                ),
            )

    return None
