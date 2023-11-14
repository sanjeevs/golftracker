import pytest
from golftracker import club_head_detector, golf_swing, club_head_params, image_utils
from unittest.mock import patch, MagicMock

# Using the patch decorator to mock scale_norm_point
@patch('golftracker.image_utils.scale_norm_point', return_value=(320, 240))
def test_club_head_detector(mock_scale_norm_point):
    # Create a mock for the golf_swing object
    mock_golf_swing = MagicMock()
    mock_golf_swing.num_frames = 10
    mock_golf_swing.height = 480
    mock_golf_swing.width = 640

    # Create a mock for the club_head_params
    mock_club_head_params = MagicMock()
    mock_club_head_params.club_head_norm_points_dict = {0: (0.5, 0.5)}

    # Initialize the ClubHeadDetector with the mocked parameters
    detector = club_head_detector.ClubHeadDetector(mock_club_head_params)

    # Call the run method
    result = detector.run(mock_golf_swing)

    # Assertions to validate the expected output
    assert result.points[0] == (320, 240), "The club head detector did not calculate the correct screen point."
    assert len(result.points) == mock_golf_swing.num_frames, "The number of frames in the result does not match the expected value."

