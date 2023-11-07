import pytest
import numpy as np
from golftracker import golf_swing as gs

# Fixture to setup GolfSwing object
@pytest.fixture
def golf_swing():
    video_input = gs.VideoInput(
        fname='video.mp4', 
        size=(1280, 720), 
        scale=1.0, 
        rotate=0
    )
    swing = gs.GolfSwing(
        height=720, 
        width=1280, 
        num_frames=30, 
        fps=30, 
        video_input=video_input
    )
    return swing

# Mock frame fixture
@pytest.fixture
def mock_frame():
    # Create a dummy frame, for example a blank image
    return np.zeros((720, 1280, 3), dtype=np.uint8)

# Test function for run_hg_line_detection
def test_run_hg_line_detection(golf_swing, mock_frame):
    lines = golf_swing.run_hg_line_detection(mock_frame)
    # Perform your tests here
    # For instance, check if the returned lines are in the expected format or not None
    assert lines is not None
    # If you know the expected lines, you can assert those as well. Example:
    # assert lines == expected_lines
