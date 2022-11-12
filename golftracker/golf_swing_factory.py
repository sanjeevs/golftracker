#
# Factory method for creating the root object
#

class GolfSwingFactory:
    def create_from_fname(fname):
        frames = convert_mp4_to_frames(fname)
        return GolfSwing(frames)

    def prototype(GolfSwing):
        """Return a new golf swing that has a deep copy of frame context.
        However the frames are a shallow copy since they are usually read only
        """
        return 

    def deep_clone(GolfSwing):
        """Return a new golf swing that is a deep copy. """
        return