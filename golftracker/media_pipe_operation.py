#
# Media pipe service that processes the frames and updates contexts.
#
import mediapipe as mp
mp_pose = mp.solutions.pose 
import cv2


def run(frames, frame_contexts):
    """Run media pipe and return frame contexts. """
    for idx, frame in enumerate(frames):
        with mp_pose.Pose(
                static_image_mode=True,
                model_complexity=2,
                enable_segmentation=True,
                min_detection_confidence=0.5,
            ) as pose:
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                frame_contexts[idx].frame_tracker.update(_create_mp_tracker(landmark))
                frame_contexts[idx].msgs.append(f"[{idx}]:MediaPipe ran successfully")
            else:
                frame_contexts[idx].msgs.append(f"[{idx}]:MediaPipe failed")


def _create_mp_tracker(landmark):
    trackers = {}
    tracker["nose"] = [landmark[mp_pose.PoseLandmark.NOSE].x,
                                landmark[mp_pose.PoseLandmark.NOSE].y]
        
    tracker["left_eye"] = [landmark[mp_pose.PoseLandmark.LEFT_EYE].x,
                            landmark[mp_pose.PoseLandmark.LEFT_EYE].y]

    tracker["right_eye"] = [landmark[mp_pose.PoseLandmark.RIGHT_EYE].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_EYE].y]

    tracker["left_ear"] = [landmark[mp_pose.PoseLandmark.LEFT_EAR].x,
                            landmark[mp_pose.PoseLandmark.LEFT_EAR].y]

    tracker["right_ear"] = [landmark[mp_pose.PoseLandmark.RIGHT_EAR].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_EAR].y]

    tracker["left_shoulder"] = [landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                            landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y]

    tracker["right_shoulder"] = [landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y]

    tracker["left_elbow"] = [landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x,
                            landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y]

    tracker["right_elbow"] = [landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y]

    tracker["left_wrist"] = [landmark[mp_pose.PoseLandmark.LEFT_WRIST].x,
                            landmark[mp_pose.PoseLandmark.LEFT_WRIST].y]

    tracker["right_wrist"] = [landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y]

    tracker["left_hip"] = [landmark[mp_pose.PoseLandmark.LEFT_HIP].x,
                            landmark[mp_pose.PoseLandmark.LEFT_HIP].y]

    tracker["right_hip"] = [landmark[mp_pose.PoseLandmark.RIGHT_HIP].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_HIP].y]

    tracker["left_knee"] = [landmark[mp_pose.PoseLandmark.LEFT_KNEE].x,
                            landmark[mp_pose.PoseLandmark.LEFT_KNEE].y]

    tracker["right_knee"] = [landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y]

    tracker["left_ankle"] = [landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                            landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y]

    tracker["right_ankle"] = [landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y]

    tracker["left_heel"] = [landmark[mp_pose.PoseLandmark.LEFT_HEEL].x,
                            landmark[mp_pose.PoseLandmark.LEFT_HEEL].y]

    tracker["right_heel"] = [landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x,
                            landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y]

    return FrameTracker(tracker)
