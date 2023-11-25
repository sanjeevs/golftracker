import json
import pytest
from golftracker import golf_swing
from golftracker import video_utils

# Make sure to import other necessary modules like media_pipe_landmarks, pose_result, etc.

# Fixture for GolfSwing object
@pytest.fixture
def golf_swing_object():
    video_input = video_utils.VideoInput(fname="example.mp4", size=(1920, 1080))
    video_spec = video_utils.VideoSpec(height=1080, width=1920, num_frames=120, fps=30, scale=1.0, rotate=0)
    return golf_swing.GolfSwing(video_spec, video_input)

# Test for the to_json method
def test_to_json(golf_swing_object, tmp_path):
    # tmp_path is a pytest fixture that provides a temporary directory unique to the test invocation
    file_path = tmp_path / "test_output.json"

    # Call the to_json method
    golf_swing_object.to_json(file_path)

    # Read the generated JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Verify the contents of the JSON file
    assert data["video_input"]["fname"] == "example.mp4"
    assert data["video_input"]["size"] == [1920, 1080]
    assert data["video_spec"]["height"] == 1080
    assert data["num_frames"] == 120
    assert len(data["mp_result"]) ==  120
    assert data["pose_result"]["handed"] == "Unknown"
    assert len(data["pose_result"]["poses"]) == 120
    assert len(data["club_head_result"]["norm_points"]) == 120
    assert len(data["club_head_result"]["algos"]) == 120


# Run the test
if __name__ == "__main__":
    pytest.main()
