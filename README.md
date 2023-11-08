# Table of Contents
1. [Introduction](#INTRODUCTION) Purpose of the package.
2. [Installation](#Installation) If you wish to use the package.
3. [Development](#Development) If you wish to change the source code and enhance the package.
4. [Distribution](#Distribution) For releasing the package to [pypi](https://pypi.org/project/golftracker/) 

## Introduction
-------------------
The goal of the process is to analyze a golf swing by processing a video that has been shot from a down-the-line perspective, which means the camera is positioned behind the golfer. The workflow consists of first capturing all the information about the swing in a pickle data base and then analyzing the swing. Below are the major steps.

### Swing Capture

#### Frame Extraction and Landmark Detection:

The video is first processed to extract all frames.
Each frame is then processed using Google MediaPipe, a machine learning framework that detects key points or "landmarks" on the golfer throughout the frames.

#### Landmark Normalization and Model Input:

The landmarks detected by Google MediaPipe, which represent various points on the golfer’s body, are input into a machine learning (ML) model.

#### Golfer Information Analysis:

The ML model analyzes the input data to deduce certain characteristics of the golfer and their swing, such as:
Determining whether the golfer is right-handed or left-handed.
Identifying the key positions of the swing: the starting pose, the top of the swing, and the ending pose.

#### Club Head Coordinate Detection:

Alongside the analysis of the golfer's body, various optical algorithms are employed to ascertain the position of the golf club head within the frames. These include:
* Hough Line Detection: This helps in identifying lines, which can be used to infer the shaft of the golf club.

* Canny Edge Detection: This identifies the edges in the images to help locate the club head.


#### Swing Arc Determination:

By combining the landmarks of the golfer's body from Google MediaPipe with the detected coordinates of the club head, the arc of the golf club's travel is deduced.

### Swing Analysis:

Finally, with an integrated set of landmarks—those of the golfer and the club head—the golf swing can be thoroughly analyzed. This analysis could reveal insights into the swing mechanics and suggest areas for improvement.

By integrating body landmarks with club head positions, this approach aims to provide a comprehensive analysis of the golf swing, potentially offering valuable feedback for improving the golfer's technique.

## Status

Currently I am working to get the club head position. Have not yet started on the analysis of the swing.

WIP: Detailed src documentation of this package is on [ReadTheDocs](https://golftracker.readthedocs.io/en/latest/)

## Installation
----------------
If you are interested in simply using the package then you can install it as a standard package. For dev look below.


```
python -m venv venv

// Activate the virtual env
// On Windows run  venv/Scripts/activate
// On Linux bash source venv/Scripts/activate.sh

pip install golftracker
```

## Status
Currently I am working on the golfswing capture portion.
The current steps are listed here [GolfSwingCapture](docs/source/golfswing_capture.md)

## Development
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

## Distribution
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