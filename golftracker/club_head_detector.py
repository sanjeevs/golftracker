'''
Detect club head in a video.
'''
from golftracker import golf_swing
from golftracker import club_head_result
from golftracker import image_utils, geom

class ClubHeadDetector:
    def __init__(self, club_head_params):
        self.params = club_head_params

    def run(self, golf_swing):
        ch_result = club_head_result.ClubHeadResult(golf_swing.num_frames)
       
        height = golf_swing.video_spec.height
        width = golf_swing.video_spec.width

        # Copy over the labels created by the user.
        for k, v in self.params.club_head_points_dict.items():
            ch_result.points[k] = v
            ch_result.algos[k] = 'Label'

        # Run the linear fit algo to esstimate the various missing ch pos.
        sublists = create_sublists_around_invalids(ch_result.algos)
        estimates = []
        for start, end in sublists:
            n = end - start - 1
            print(f"n={n}")
            if ch_result.algos[start] != "Invalid" and ch_result.algos[end] != "Invalid":
                estimates = geom.split_line(ch_result.points[start], ch_result.points[end], n + 1)
                idx = 0
                for i in range(start + 1, end):
                    ch_result.points[i] = estimates[idx]
                    ch_result.algos[i] = "LinearFit"
                    idx += 1
        
        return ch_result



def find_consecutive_invalid_indices(algos, start_idx=0):
    """
    Find a sublist of invalid algorithm entries in a list.
    Returns:
    (tuple): The start and end index including both ie [a, b].
             Returns (None, None) under invalid cases.
    """
    try:
        # Find the index of the first occurrence of 1
        start = algos.index('Invalid', start_idx)

        # Find the index of the next occurrence of 2 after the index of 1
        end = start
        while end < len(algos) and algos[end] == "Invalid":
            end += 1

        return start, end -1
    except ValueError:
        return None, None


def create_sublists_around_invalids(algos):
    """
    Splits the list into sublists based on algos=Invalid.
    """
    num_frames = len(algos)
    max_value = num_frames - 1
    start_idx = 0
    result = []
    def in_between(x, n, m):
        return n <= x <= m

    while True:
        print(f"algos={algos}")
        start, end = find_consecutive_invalid_indices(algos, start_idx)
        if start and in_between(start, 0, max_value) \
                and in_between(end, 0, max_value -1):
            sublist_start = max(0, start -1)
            sublist_end = min(end + 1, max_value)
            result.append((sublist_start, sublist_end))
            start_idx = end + 1
            continue
        else:
            break
    return result


