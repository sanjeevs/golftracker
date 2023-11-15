from golftracker import golf_swing_repository
from golftracker import golf_swing_factory
from golftracker import video_utils

import os

def test_export(tmp_path):
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')
    video_input = video_utils.VideoInput(fname=fname, size=os.path.getsize(fname))
    (frames, video_spec) = video_utils.split_video_to_frames(fname)
    gs = golf_swing_factory.create_from_video(video_input, video_spec, frames)
   
    assert gs.video_input.fname == os.path.join('tests', 'assets', 'test_blank_3.mov')
    video_size = gs.video_input.size
    db = tmp_path / "gs.pkl"
    golf_swing_repository.serialize(db, gs)

    #new_gs = golf_swing_repository.reconstitute(db, search_lst=[os.path.join('tests', 'assets')])
    new_gs = golf_swing_repository.reconstitute(db)
    assert new_gs.video_spec.height == 100
    assert new_gs.video_spec.width == 200
    assert new_gs.video_spec.num_frames == 3
    assert new_gs.video_input.size == video_size

def test_search_path(tmp_path):
    fname = os.path.join('tests', 'assets', 'test_blank_3.mov')

    video_input = video_utils.VideoInput(fname=fname, size=os.path.getsize(fname))
    (frames, video_spec) = video_utils.split_video_to_frames(fname)
    gs = golf_swing_factory.create_from_video(video_input, video_spec, frames)
    # Clobber the path to the mov file.
    gs.video_fname = 'test_blank_3.mov'
    video_size = gs.video_input.size

    db = tmp_path / "gs.pkl"
    golf_swing_repository.serialize(db, gs)

    new_gs = golf_swing_repository.reconstitute(db, search_lst=[os.path.join('tests', 'assets')])
    assert new_gs.video_spec.height == 100
    assert new_gs.video_spec.width == 200
    assert new_gs.video_spec.num_frames == 3
    assert new_gs.video_input.size == video_size
    assert new_gs.video_input.fname == os.path.join('tests', 'assets', 'test_blank_3.mov')