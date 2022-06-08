.. golftracker documentation master file, created by
   sphinx-quickstart on Wed Jun  1 18:59:52 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to golftracker's documentation!
=========================================
This package is used to detect the various elements in a golf swing. It does this by using open cv to detect motion. These points on the frames are referred to as trackers.

The problem of detection can be broken into 2 steps.
1. Detect the initial position of the tracker in the first frame. 
2. Given the position of the tracker in the previous frame, detect the movement in the current frame.

These tracker are written out in json file for the *golftrainer* package to analyze.

Version 1
----------------
In this version only the initial ball position and the postion of the club shaft are tracked in each frame.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tracker
   golfeditor
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
