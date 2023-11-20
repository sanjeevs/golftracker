import pytest
from golftracker import club_head_detector, golf_swing, club_head_params, image_utils
from golftracker import club_head_result
from unittest.mock import patch, MagicMock

def test_club_head_detector():
    # Create a mock for the golf_swing object
    mock_golf_swing = MagicMock()
    mock_golf_swing.num_frames = 10
    mock_golf_swing.height = 480
    mock_golf_swing.width = 640

    # Create a mock for the club_head_params
    mock_club_head_params = MagicMock()
    mock_club_head_params.club_head_points_dict = {0: (320, 240)}

    # Initialize the ClubHeadDetector with the mocked parameters
    detector = club_head_detector.ClubHeadDetector(mock_club_head_params)
    assert detector.params == mock_club_head_params

def test_invalid_sublist():
    algos = ["Invalid", "Invalid", "Linear"]
    start, end = club_head_detector.find_consecutive_invalid_indices(algos)
    assert start == 0
    assert end == 1

def test_split_invalid_algos_1():
    algos = ["x", "Invalid", "Invalid", "Linear"]
    result = club_head_detector.create_sublists_around_invalids(algos)
    assert len(result) == 1
    assert result[0] == (0, 3)

def test_split_invalid_algos_2():
    algos = ["x", "Invalid", "Invalid", "y", "Invalid", "Invalid", "z"]
    result = club_head_detector.create_sublists_around_invalids(algos)
    assert len(result) == 2
    assert result[0] == (0, 3)
    assert result[1] == (3, 6)

def test_failing_consec_indices():
    algos = ["x", "Invalid", "Invalid", "Invalid", "Invalid", "y"]
    result = club_head_detector.find_consecutive_invalid_indices(algos)
    assert result == (1, 4)

def test_split_invalid_algos_3():
    algos = ["x", "Invalid", "Invalid", "Invalid", "Invalid", "y"]
    result = club_head_detector.create_sublists_around_invalids(algos)
    assert len(result) == 1
    assert result[0] == (0, 5)

def test_invalid_split1():
    algos = ["Invalid", "Invalid", "Linear"]
    result = club_head_detector.create_sublists_around_invalids(algos)
    assert result == []

    algos = ["x", "Invalid", "Invalid"]
    result = club_head_detector.create_sublists_around_invalids(algos)
    assert result == []