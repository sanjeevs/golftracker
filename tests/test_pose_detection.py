from golftracker import pose_detection
import pytest

def test_main():
    with pytest.raises(SystemExit) as exc:
        pd = pose_detection.main()
