#
# Root object.
# Constraint: length of frames == length of frame contexts
# Collection of tuples (frame, frame_context)

import frame_context
import media_pipe_operation as mp_op


class GolfSwing:
    def __init__(self, frames):
        self.frames = frames
        self.frame_contexts = []
        for _ in range(len(frames)):
            self.frame_contexts.append(frame_context.FrameContext())

    def run_media_pipe(self):
        """ Run media pipe algo on the frames and update the frame context. """
        mp_op.run(self.frames, self.frame_contexts)

    def save_context_to_json(self, json_fname):
        """ Save frame context to a json fname. """
        json.dump(self.frame_contexts)