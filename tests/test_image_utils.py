from golftracker import image_utils
import pytest

def test_scale_norm():
    p = image_utils.scale_norm_point((0.5, 0.5), width=100, height=200)
    assert p == (50, 100)

def test_norm_2_screen():
    # Test with dictionary
    obj = image_utils
    assert obj.norm_2_screen({'point1': (0.5, 0.5), 'point2': (1, 1)}, 100, 200) \
            == {'point1': (50, 100), 'point2': (100, 200)}

    # Test with list
    assert obj.norm_2_screen([(0.5, 0.5), (1, 1)], 100, 200) == [(50, 100), (100, 200)]

    # Test with tuple
    assert obj.norm_2_screen((0.5, 0.5), 100, 200) == (50, 100)

    # Test with unsupported type
    with pytest.raises(TypeError):
        obj.norm_2_screen("not a valid input", 100, 200)    