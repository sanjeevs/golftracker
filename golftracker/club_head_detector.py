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
        print(f"algos={ch_result.algos}")
        print(f"sublists={sublists}")
        estimates = []
        for start, end in sublists:
            n = end - start - 1
            print(f"Detector:n={n}, start={start}, end={end}")
            estimates = geom.split_line(ch_result.points[start], ch_result.points[end], n)
            print(f"Estimates={estimates}")

        for start, end in sublists:
            idx = 0
            for i in range(start + 1, end):
                print(f"Updaing start={start}, end={end}, {i}")
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

        print(f"find_consec:start={start}, end={end -1}")
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
        start, end = find_consecutive_invalid_indices(algos, start_idx)
        if start and in_between(start, 1, max_value) \
                and in_between(end, 2, max_value -1):
            result.append((start -1, end + 1))
            start_idx = end + 1
            continue
        else:
            break
    return result


