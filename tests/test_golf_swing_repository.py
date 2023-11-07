from golftracker import golf_swing_repository
from golftracker import golf_swing_factory
from golftracker import video_utils

import os

def test_export(tmp_path):
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')

    frames, gs = golf_swing_factory.create_from_video(fname)
    assert gs.video_input.fname == os.path.join('tests', 'assets', 'test_blank_3.mov')
    video_size = gs.video_input.size
    db = tmp_path / "gs.pkl"
    golf_swing_repository.serialize(db, gs)

    #new_gs = golf_swing_repository.reconstitute(db, search_lst=[os.path.join('tests', 'assets')])
    new_gs = golf_swing_repository.reconstitute(db)
    assert new_gs.height == 100
    assert new_gs.width == 200
    assert new_gs.num_frames == 3
    assert new_gs.video_input.size == video_size

def test_search_path(tmp_path):
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')

    frames, gs = golf_swing_factory.create_from_video(fname)
    # Clobber the path to the mov file.
    gs.video_fname = 'test_blank_3.mov'
    video_size = gs.video_input.size

    db = tmp_path / "gs.pkl"
    golf_swing_repository.serialize(db, gs)

    new_gs = golf_swing_repository.reconstitute(db, search_lst=[os.path.join('tests', 'assets')])
    assert new_gs.height == 100
    assert new_gs.width == 200
    assert new_gs.num_frames == 3
    assert new_gs.video_input.size == video_size
    assert new_gs.video_input.fname == os.path.join('tests', 'assets', 'test_blank_3.mov')