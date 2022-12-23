from golftracker import golf_swing_repository
from golftracker import golf_swing_factory
import os

def test_export(tmp_path):
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    gs = golf_swing_factory.create_from_video(fname, pose_model = None)

    db = tmp_path / "gs.pkl"
    golf_swing_repository.serialize(db, gs)
    new_gs = golf_swing_repository.reconstitute(db, os.path.join('tests', 'assets'))
    assert new_gs.height == 100
    assert new_gs.width == 200
    assert new_gs.num_frames == 3