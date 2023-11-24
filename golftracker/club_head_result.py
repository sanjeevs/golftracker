'''
Result of the club head detector.
'''
import copy


class ClubHeadResult:
    def __init__(self, num_frames):
        self.norm_points = [None] * num_frames
        self.algos = ["Invalid"] * num_frames

    def update(self, new):
        for i, point in enumerate(new.norm_points):
            if point:
                self.norm_points[i], self.algos[i] = point, new.algos[i]

    def reset_and_update(self, new):
        self.norm_points, self.algos = new.norm_points.copy(), new.algos.copy()

    def __str__(self):
        valid_points = [(i, pt) for i, pt in enumerate(self.norm_points) if pt]
        num_labels = sum([1 for algo in self.algos if algo != "Invalid"])
        return f"Found {len(valid_points)} club head points with {num_labels} valid"

    def export_lst(self):
        lst = []
        for idx, point in enumerate(self.norm_points):
            if point == None:
                lst.append([0, 0, "Invalid"])
            else:
                lst.append([point[0], point[1], self.algos[idx]])

        return ["x", "y", "algo"], lst

    def import_lst(self, lst):
        for idx, entry in enumerate(lst):
            x, y = int(entry[0]), int(entry[1])
            if x == 0 and y == 0:
                self.norm_points[idx] = None
                self.algos[idx] = "Invalid"
            else:
                self.norm_points[idx] = (x, y)
                self.algos[idx] = entry[2]

