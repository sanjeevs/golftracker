Introduction
==============
This package detects the various elements in a golf swing. It does this by tracking various points in the swing and 
writing the coordinates into a json file for later processing.

No single algorithm can generate all the trackers in a frame. Hence multiple algorithms are run, which creates multiple
json files per frame. These are then merged to create a single composite json file per frame.

The various algorithm used are
* [Google Media Pipe Pose Detection](https://google.github.io/mediapipe/solutions/pose) This detects 33 pose landmarks.
These are written into json files with filename <frame_fname>_mp.json


* Use the script golfeditor in this package to mark the position of the ball and the club head initially. Then run the
cv2 tracking algorithms to track the movements of these across multiple frames. The trackers tracked by this are
  1. Club Grip: This is where the hands are holding the club shaft.
  2. Club Heel: This is shown in this  [diagram](https://www.golfdistillery.com/definitions/club-parts/heel/#:~:text=The%20heel%20is%20a%20specific,located%20nearer%20to%20the%20golfer.)
  3. Club Toe : Shown [here](https://www.golfdistillery.com/definitions/club-parts/toe/#:~:text=The%20toe%20is%20a%20specific,located%20farthest%20from%20the%20golfer.)
  4. Position of the golf ball.
  
Detailed src documentation of this package is on [ReadTheDocs](https://golftracker.readthedocs.io/en/latest/)

Installation
=============
This is a standard python package and follows the typical flow for installing python packages.

```
python -m venv env_test_tracker

// Activate the virtual env
// On Windows run  env_test_tracker/Scripts/activate
// On Linux bash source env_test_tracker/Scripts/activate.sh

pip install golftracker
```

To run the example below you would also need another utility package thatI use
for video file manipulations.
```
pip install spvidoeutils
```

Development
===============
The source repository is in [GitHub](https://github.com/sanjeevs/golftracker). The development flow is similar to other python
projects.
* Clone the project.
* Create a virtual env and install all the dependencies
* Install the package locally in dev mode.

Distribution
=========================
This is a pure python code package and so a wheel distribution is sufficient.
My typical steps are below.
* Bump the version in setup.py
* Build the distribution
```commandline
python setup.py bdist_wheel
```
* Upload the distribution
```commandline
twine upload dist/*
```

Example
===========
I downloaded a video of [michelle wei swing side view](https://www.youtube.com/watch?v=6LuiISfKa3o) and used the following 
flow to create the tracker. 

The shortened copy of the video is also on my shared drive as 
https://drive.google.com/file/d/16TaL8PSaK46wbXr7mVsDZLbpOieLC3Nm/view?usp=sharing

Let's save/rename it as test1.mp4 for the steps below.

## Step1: Split the video into frames
From the package spvideoutils, run the script  *video_split* to create a subdir *test1* that will have all the frames.

```
video_split test1.mp4

```


## Step2: Run Google media script to create json
Run the command below to create the json file for the trackers by google pose detection.
```commandline
pose_detection test1
```

## Step3: Run golf detection tracker.
For this the first step is to use the script *golfeditor* to manually select
the club grip, club heel and club toe of the first frame.

Use the following keywords to select the corresponding tracker. Press 's' to save to json

| Key | Description |
|-----|-------------|
 |b | ball selected|
 |g | club grip |
 |h | club heel |
 |t | club toe |
 |s | save to json|

```commandline
golfeditor test1
```
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

   
