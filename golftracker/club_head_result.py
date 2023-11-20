'''
Result of the club head detector.
'''
import copy


class ClubHeadResult:
    def __init__(self, num_frames):
        self.points = [None] * num_frames
        self.algos = ["Invalid"] * num_frames

    def update(self, new):
        for i, point in enumerate(new.points):
            if point:
                self.points[i], self.algos[i] = point, new.algos[i]

    def reset_and_update(self, new):
        self.points, self.algos = new.points.copy(), new.algos.copy()

    def __str__(self):
        valid_points = [(i, pt) for i, pt in enumerate(self.points) if pt]
        return f"Found {len(valid_points)} club head points: {valid_points}"

    def export_lst(self):
        lst = []
        for idx, point in enumerate(self.points):
            if point == None:
                lst.append([0, 0, "Invalid"])
            else:
                lst.append([point[0], point[1], self.algos[idx]])

        return ["x", "y", "algo"], lst

    def import_lst(self, lst):
        for idx, entry in enumerate(lst):
            if entry[0] == 0 and entry[1] == 0:
                self.points[idx] = None
                self.algos = "Invalid"
            else:
                self.points[idx] = (entry[0], entry[1])
                self.algos[idx] = entry[2]