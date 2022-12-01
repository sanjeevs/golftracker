from golftracker import gt_const

def test_pose_header():
    row_header = gt_const.pose_row_header()

    assert len(row_header) == 33 * 4
    assert row_header[0] == "nose_x"