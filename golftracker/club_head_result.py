'''
Result of the club head detector.
'''

class ClubHeadResult:
    def __init__(self, num_frames):
        self.points = [None] * num_frames

    def update(self, new):
        for i in range(len(new.points)):
            if new.points[i]:
                self.points[i] = new.points[i]
        

    def reset_and_update(self, new):
        """
        Clears the original list and updates it with elements from the new list.
        """
        self.points.clear()
        self.points.extend(new.points)

    def __str__(self):
        not_none = [(i, pt) for i, pt in enumerate(self.points) if pt is not None]
        return f"Found {len(not_none)} club head points. {not_none}"