import pytest
from golftracker.club_head_detector import find_consecutive_invalid_indices, create_sublists_around_invalids

# Tests for find_consecutive_invalid_indices
@pytest.mark.parametrize("algos, start_idx, expected", [
    ([], 0, (None, None)),  # Test Empty List
    (['Valid', 'Valid'], 0, (None, None)),  # Test No Invalid Entries
    (['Invalid'], 0, (0, 0)),  # Test Single Invalid Entry
    (['Invalid', 'Invalid', 'Valid'], 0, (0, 1)),  # Test Multiple Consecutive Invalid Entries
    (['Valid', 'Invalid', 'Invalid'], 0, (1, 2)),  # Test Invalid Entries Not at Start
    (['Valid', 'Invalid', 'Invalid'], 1, (1, 2)),  # Test with Start Index
    (['Valid', 'Invalid', 'Valid'], 0, (1, 1)),  # Test fail
    (['Valid', 'Valid'], 2, (None, None)),  # Test Out-of-Bounds Start Index
    (['Invalid', 'Invalid', 'Label', 'Invalid', 'Invalid', 'Label', 'Invalid'], 0, (0, 1)),
    (['Invalid', 'Invalid', 'Label', 'Invalid', 'Invalid', 'Label', 'Invalid'], 2, (3, 4)),
    (['Invalid', 'Invalid', 'Label', 'Invalid', 'Invalid', 'Label', 'Invalid'], 3, (3, 4)),
    (['Invalid', 'Invalid', 'Label', 'Invalid', 'Invalid', 'Label', 'Invalid'], 4, (4, 4)),
])
def test_find_consecutive_invalid_indices(algos, start_idx, expected):
    assert find_consecutive_invalid_indices(algos, start_idx) == expected

# Tests for create_sublists_around_invalids
@pytest.mark.parametrize("algos, expected", [
    ([], []),  # Test Empty List
    (['Valid'], []),  # Test No Invalid Entries
    (['Valid', 'Invalid', 'Valid'], [(0, 2)]),  # Test Single Invalid Entry
    (['Valid', 'Invalid', 'Valid', 'Invalid', 'Valid'], [(0, 2), (2, 4)]),  # Test Multiple Non-Consecutive Invalid Entries
    (['Valid', 'Invalid', 'Invalid', 'Valid'], [(0, 3)]),  # Test Multiple Consecutive Invalid Entries
    (['Invalid', 'Valid', 'Invalid'], []),  # Test Edge Case: Invalid at Start
    (['Valid', 'Invalid', 'Invalid'], []),  # Test Edge Case: Invalid at End
    (['Invalid', 'Invalid', 'Label', 'Invalid', 'Invalid', 'Label', 'Invalid'], [(2, 5)]),
])
def test_create_sublists_around_invalids(algos, expected):
    assert create_sublists_around_invalids(algos) == expected
