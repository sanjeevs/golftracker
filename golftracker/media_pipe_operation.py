#
# Media pipe service that processes the frames and updates contexts.
#
import mediapipe as mp
mp_pose = mp.solutions.pose 
import cv2

import frame_tracker


def run(frames, frame_contexts):
    """Run media pipe and return frame contexts. """
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
                frame_contexts[idx].frame_tracker.update(_create_mp_tracker(landmark))
                frame_contexts[idx].msgs.append(f"[{idx}]:MediaPipe ran successfully")
            else:
                frame_contexts[idx].msgs.append(f"[{idx}]:MediaPipe failed")


def _create_mp_tracker(landmark):
    trackers = {}
    trackers["nose"] = [landmark[mp_pose.PoseLandmark.NOSE].x,
                                landmark[mp_pose.PoseLandmark.NOSE].y]
        
    trackers["left_eye"] = [landmark[mp_pose.PoseLandmark.LEFT_EYE].x,
                            landmark[mp_pose.PoseLandmark.LEFT_EYE].y]

    trackers["right_eye"] = [landmark[mp_pose.PoseLandmark.RIGHT_EYE].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_EYE].y]

    trackers["left_ear"] = [landmark[mp_pose.PoseLandmark.LEFT_EAR].x,
                            landmark[mp_pose.PoseLandmark.LEFT_EAR].y]

    trackers["right_ear"] = [landmark[mp_pose.PoseLandmark.RIGHT_EAR].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_EAR].y]

    trackers["left_shoulder"] = [landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                            landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y]

    trackers["right_shoulder"] = [landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y]

    trackers["left_elbow"] = [landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                            landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y]

    trackers["right_elbow"] = [landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y]

    trackers["left_wrist"] = [landmark[mp_pose.PoseLandmark.LEFT_WRIST].x,
                            landmark[mp_pose.PoseLandmark.LEFT_WRIST].y]

    trackers["right_wrist"] = [landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y]

    trackers["left_hip"] = [landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                            landmark[mp_pose.PoseLandmark.LEFT_HIP].y]

    trackers["right_hip"] = [landmark[mp_pose.PoseLandmark.RIGHT_HIP].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_HIP].y]

    trackers["left_knee"] = [landmark[mp_pose.PoseLandmark.LEFT_KNEE].x,
                            landmark[mp_pose.PoseLandmark.LEFT_KNEE].y]

    trackers["right_knee"] = [landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]

    trackers["left_ankle"] = [landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                            landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y]

    trackers["right_ankle"] = [landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y]

    trackers["left_heel"] = [landmark[mp_pose.PoseLandmark.LEFT_HEEL].x,
                            landmark[mp_pose.PoseLandmark.LEFT_HEEL].y]

    trackers["right_heel"] = [landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y]

    return frame_tracker.FrameTracker(trackers)
