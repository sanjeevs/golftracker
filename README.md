# Table of Contents
1. [Introduction](#INTRODUCTION) Purpose of the package.
2. [Installation](#Installation) If you wish to use the package.
3. [Development](#Development) If you wish to change the source code and enhance the package.
4. [Distribution](#Distribution) For releasing the package to [pypi](https://pypi.org/project/golftracker/) 

Introduction
-------------------
Analyze a golf swing video and analyze the various components of a golf swing.
The video is expected to be shot in "down the line" format and can be of any reasonable resolution.

For ease of analysis, I usually scale down the input frames to Width of 500 pixels, keeping the same aspect ratio, but code should work on any larger sizes.

Possible uses 

The various algorithm used are
* [Google Media Pipe Pose Detection](https://google.github.io/mediapipe/solutions/pose) This detects 33 pose landmarks.

* sklearn ml model to classify start pose, top pose and end poses.

* cv2 for tracking the golf club. The points tracked are

  1. Club Heel: This is shown in this  [diagram](https://www.golfdistillery.com/definitions/club-parts/heel/#:~:text=The%20heel%20is%20a%20specific,located%20nearer%20to%20the%20golfer.)
  2. Club Toe : Shown [here](https://www.golfdistillery.com/definitions/club-parts/toe/#:~:text=The%20toe%20is%20a%20specific,located%20farthest%20from%20the%20golfer.)

Detailed src documentation of this package is on [ReadTheDocs](https://golftracker.readthedocs.io/en/latest/)

Installation
----------------
If you are interested in simply using the package then you can install it as a standard package. For dev look below.


```
python -m venv env_test_tracker

// Activate the virtual env
// On Windows run  env_test_tracker/Scripts/activate
// On Linux bash source env_test_tracker/Scripts/activate.sh

pip install golftracker
```

Development
---------------
The source repository is in [GitHub](https://github.com/sanjeevs/golftracker). The development flow is similar to other python
projects.
* Clone the project.
```
git clone https://github.com/sanjeevs/golftracker.git
```
* Create a virtual env and install all the dependencies
```
venv>  pip install -r requirements.txt
```
* Run unit tests for sanity
```
(venv)golftracker> pytest
```
* Install the package locally for development.
```
 pip install -e .
```

Distribution
------------------------
For publishing this package on pypy use the following steps.
* Bump the version in setup.py
* Build the distribution
```commandline
python setup.py bdist_wheel
```
* Upload the distribution
```commandline
twine upload dist/*
```