'''
Result of the club head detector.
'''

class ClubHeadResult:
    def __init__(self, num_frames):
        self.points = [None] * num_frames

    def merge_with_preserve(self, new):
        """
        Merges two lists, preserving non-None values in the original list.
        Only None values in the original list are replaced by corresponding values in the new list.
        """
        for i in range(min(len(self.points), len(new))):
            if self.points[i] is None:
                self.points[i] = new[i]

    def replace_all(self, new):
        """
        Replaces all elements of the original list with elements from the new list.
        Assumes both lists are of the same length.
        """
        for i in range(len(self.points)):
            self.points[i] = new[i]


    def reset_and_update(self, new):
        """
        Clears the original list and updates it with elements from the new list.
        """
        self.points.clear()
        self.points.extend(new)