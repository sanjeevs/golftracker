Introduction
==============
This package detects the various elements in a golf swing. It does this by tracking various points in the swing and outputing it into a json file.

The package provides various algorithms for creating different trackers. Each of these tracker write out the information in a json file. At the end all the json files are merged to create a final json file for each of the frames.

The various algorithm used are
* [Google Media Pipe Pose Detection](https://google.github.io/mediapipe/solutions/pose) This detects 33 pose landmarks.
* Use the script golfeditor in this package to mark the position of the ball and the club head.

Detailed src documentatin is on [ReadTheDocs](https://golftracker.readthedocs.io/en/latest/)

Installation
=============
The package provides cmd line utilities for creating the trackers on the video frame.
To install the package you can create a virtual env and install the package. For example

```
python -m venv env_test_tracker
// Activate the virtual env
pip install golftracker
```

Example
===========
I downloaded a video of [michelle wei swing side view](https://www.youtube.com/watch?v=6LuiISfKa3o) and used the following flow to create the tracker. 

The copy of the video is also on my shared drive as 
https://drive.google.com/drive/folders/1Q3bAIHYQXX3f0yl_jR7Bco0MpYRop3sS?usp=sharing

## Step1: Split the video into frames
For this install the helper package.  Run the script *video_crop* to create shortened video file and then use *video_split* to create the frames.

```
pip install spvidoeutils
video_crop -s 66 michelle_wie_side_video.mp4 -o test1.mp4
video_split test1.mp4

```
This creates a folder called test1 and stores each frame sequentially as png file.

## Step2: Run Google media script to create json
This step allows the user to create the json file by hand.

Trackers
============
The following points are tracked on each frame as points with co ordindates (x,y).
They are written into a json file for further analysis.

* Ball Position
  This is the point at which the ball is placed. It is assumed that the target is directly towards it.


* Club Shaft Position
  The start of the club is where the hands grasp the shaft and the end is where the club head is

Json Output
=============
A sample json output is shown below for a frame with width=1024 and height=900. The coordinates assume that left top is the origin.

The ball is placed at (100, 200). The hand holding the shaft is at (10, 20) and the club head is at (30, 40)
```commandline
{
    "frame" : [1024, 900]
	  "ball": [1, 2],
	  "shaft": [10, 20, 30, 40]
}
```

   
