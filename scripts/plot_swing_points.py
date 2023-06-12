'''
Plot the various swing points.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse

from golftracker import golf_swing_repository
from golftracker import path_model
from golftracker import video_utils
from golftracker import image_utils
from golftracker import geom
from golftracker import golf_swing as gs

def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Display the golf swing from the pkl data base"
    )

    parser.add_argument("swing_db", type=str, help="Input golf swing data base")

    return parser


def main():
    opt = create_parser().parse_args()
    gs = golf_swing_repository.reconstitute(opt.swing_db)
    
    (video_frames, _) = video_utils.split_video_to_frames(gs.video_fname)
    if len(video_frames) == 0:
        raise ValueError(f"No frames detected in '{gs.video_fname}'")
    
    idx = 0
    key_pressed = ''

    right_thumb_path = path_model.get_path(gs, "right_thumb")
    right_elbow_path = path_model.get_path(gs, "right_elbow")
    right_shoulder_path = path_model.get_path(gs, "right_shoulder")
    nose_path = path_model.get_path(gs, "nose")

    lb_right_thumb_path = [geom.origin_to_lb(x, y, gs.width, gs.height) for x, y in right_thumb_path]
    lb_right_elbow_path = [geom.origin_to_lb(x, y, gs.width, gs.height) for x, y in right_elbow_path]
    lb_right_shoulder_path = [geom.origin_to_lb(x, y, gs.width, gs.height) for x, y in right_shoulder_path]
    lb_nose_path = [geom.origin_to_lb(x, y, gs.width, gs.height) for x, y in nose_path]
    velocities = geom.compute_velocities(lb_right_thumb_path, gs.fps)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    plt.subplots_adjust(left=0.1, right=0.9, hspace=0.3)

    colors = ['b', 'g', 'r', 'c']
    point_labels = ['shoulder', 'elbow', 'thumb', 'nose']

    def update_plot(frame, paths, vel):
        nonlocal idx
        frame_index_text = f"Frame: {idx}"
        frame = cv2.putText(frame, frame_index_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                            (255, 255, 255), 2, cv2.LINE_AA)
        if len(paths[0]) > 0:
            frame = cv2.circle(frame, right_thumb_path[idx-1], radius=10, color=(0, 0, 255), thickness=-1)
            frame = cv2.circle(frame, right_elbow_path[idx-1], radius=10, color=(0, 255, 0), thickness=-1)
            frame = cv2.circle(frame, right_shoulder_path[idx-1], radius=10, color=(255, 0, 0), thickness=-1)


        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        ax1.imshow(frame)

        for artist in ax2.collections + ax2.lines:
            artist.remove()
        for artist in ax3.collections + ax3.lines:
            artist.remove()

      
        for artist in ax4.collections + ax4.lines:
            artist.remove()
        ax4.plot([lb_right_shoulder_path[0][0], lb_right_elbow_path[0][0], lb_right_thumb_path[0][0]],
                 [lb_right_shoulder_path[0][1], lb_right_elbow_path[0][1], lb_right_thumb_path[0][1]],
                 linestyle='--', marker='o')
        for i, path in enumerate(paths):
            for j, pos in enumerate(path):
                ax2.plot(pos[0], pos[1], marker='o', markersize=1, color=colors[i % len(colors)], 
                        label=point_labels[i % len(point_labels)])
                if j > 0:
                    ax2.plot(
                        [path[j - 1][0], pos[0]],
                        [path[j - 1][1], pos[1]],
                        linestyle='--',
                        color=colors[i % len(colors)]
                    )
        times = np.arange(len(vel))
        ax3.plot(times, vel, linestyle='--', color='r', label='ThumbVelocity')

        ax4.plot([lb_right_shoulder_path[idx][0], lb_right_elbow_path[idx][0], lb_right_thumb_path[idx][0]],
                 [lb_right_shoulder_path[idx][1], lb_right_elbow_path[idx][1], lb_right_thumb_path[idx][1]],
                 linestyle='--', marker='o'
        )
        handles, labels = ax2.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax2.legend(by_label.values(), by_label.keys())

        fig.canvas.draw_idle()

    ax1.axis('off')
    ax2.set_xlim(0, gs.width)
    ax2.set_ylim(0, gs.height)
    ax2.set_title("Point Positions")
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax3.set_title("Velocity")
    ax4.set_xlim(0, gs.width)
    ax4.set_ylim(0, gs.height)
    ax4.set_title("ShoulderElbowThumb")
    update_plot(video_frames[idx], [lb_right_shoulder_path[0:idx], lb_right_elbow_path[0:idx],
                                    lb_right_thumb_path[0:idx], lb_nose_path[0:idx]], 
                velocities[0:idx])

    def press(event):
        nonlocal idx
        if event.key == "right" or event.key == "n":
            if event.key == "right":
                idx = min(idx + 1, gs.num_frames -1)
            else:
                idx = min(idx + 10, gs.num_frames -1)
        elif event.key == "left" or event.key == "p":
            if event.key == "left":
                idx = max(idx -1, 0)
            else:
                idx = max(idx -10, 0)
        update_plot(video_frames[idx], [lb_right_shoulder_path[0:idx], lb_right_elbow_path[0:idx],
                                    lb_right_thumb_path[0:idx], lb_nose_path[0:idx]], 
                velocities[0:idx])
       
       
    fig.canvas.mpl_connect('key_press_event', press)
    plt.show()


if __name__ == "__main__":
    main()
            