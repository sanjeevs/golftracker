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

* To install locally for development.
```commandline
pip install -e .
```

Example
===========
In this example we will take a youtube video of [michelle wei swing side view](https://www.youtube.com/watch?v=6LuiISfKa3o) 
and detect various interesting objects during the swing. The resultant information will
be subsequently fed into a golf swing model that can detect various parameters from it.

In this package we are only going to create a output video that will be used as input 
to the golf swing model.

The shortened copy of the video is also on my shared drive as 
https://drive.google.com/file/d/16TaL8PSaK46wbXr7mVsDZLbpOieLC3Nm/view?usp=sharing

Let's create a directory *example1* and save/rename it as test1.mp4 in the dir for the steps below.

## Step1: Split the video into frames
From the package spvideoutils, run the script  *video_split* to create a subdir *test1* that will have all the frames.

```
video_split test1.mp4

```


## Step2: Google Pose Detection
Run the command below to create the json file for the trackers by google pose detection.
```commandline
pose_detection test1
```
The default json file generated will be of the name *frame_nnn_mp.json* .

## Step3: Initial Detection for CV2 Tracking
For this the first step is to use the script *golfeditor* to manually select
the club grip, club heel and club toe of the first frame. These coordinates are
fed to open cv object detection that creates the json file for subsequent frames.

```commandline
golfeditor test1
```

Use the following keywords to select the corresponding tracker. Press 's' to save 
the initial json for the first frame. The default file name will be frame_nnn_od.json

| Key | Description |
|-----|-------------|
 |b | ball selected|
 |g | club grip |
 |h | club heel |
 |t | club toe |
 |s | save to json|


## Step 4: CV2 Tracking
Run open cv object detection given the last known position. By default, the script will 
use the highest frame_nnn_od.json as the starting point for subsequent frames. It is possible
to override this behavior by passing the initial position using the -i argument.

Different algorithms will return different results. The script will merge the results and write 
out a single json file per frame. It is possible that only certain objects or no objects are
detected in each frame. In such cases the previous known position is written out and 
warning printed.

```commandline
obj_detection test1 
```

## Step 5: Json Merge
At this stage each frame 'nnn' has 2 json files associated with it.
* frame_nnn_mp.json: Google media pipe detection
* frame_nnn_od.json: Open CV object detection
These need to be merged to create a single json file for a frame. The default name of
the json file will be frame_nnn.json.

```commandline
merge_json test1
```
## Step 6: Visualize
The result json files can be visualized by converting to png files. These can be 
then merged into a single video mp4 file for visualization.

By default the output png files are called *out_nnn.png*
```commandline
gd_visualize test1
```
To merge the output png files into a mp4 file use the utility from spvideoutils.
```commandline
merge_video test1 -m out -o out.mp4
```
## Step 7: Summary
Using the above steps we have taken a video of a swing, ran it through a bunch
of algorithms to detect the various interesting points and written out a new mp4 file called out.mp4

Run the video to see that what the golf model will use to analyze the swing.

   
