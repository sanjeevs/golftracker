.. golftracker documentation master file, created by
   sphinx-quickstart on Wed Jun  1 18:59:52 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to golftracker's documentation!
=========================================
This package package is used to analyze a golf swing video and provide useful feedback for improvement.

It uses the following python packages.

* `cv2`_

  Use for video maninpulations, line detection and object tracking algorithms

* `media_pipe`_

  Google media pipe for pose detection.

* `ml_model`_
   
  Machine learning model from scikit. By default I use RandomForestClassifier pipeline.

The general flow can be broken into 2 phases as shown below. The first process creates the golf swing model. This is analyzed and the results for the swing returned to the user. The user can then view the output annotated video for reference.

.. image:: /images/golftracker.svg

.. warning:: This version is restricted to videos of right handed golf swings shot down the line.

Quick Start
-------------
To use the GolfTracker package, you can simply install it as a standard package. Follow the steps below:


1. Create a virtual environment for your project.

     python -m venv env_test_tracker



2. Activate the virtual environment
    * Windows
        env_test_tracker\Scripts\activate

    * Linux
        source env_test_tracker/bin/activate

3. Once the virtual environment is activated, you can install the GolfTracker package using pip:
     pip install golftracker

Contributing
--------------------
If you want to contribute to the development of the GolfTracker package, you should follow these additional steps:

1. Clone the repository:
2. Create a virtual environment for development:
3. Activate the virtual environment as described above.
4. Install the development dependencies:
5. You can now start developing and contribute to the package.


More Details
--------------
For more details refer to the links below.

.. toctree::
    scripts
    architecture

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
 autoapi/index
 :maxdepth: 5

.. _cv2: http://opencv.org
.. _media_pipe: https://google.github.io/mediapipe/
.. _ml_model: https://scikit-learn.org/stable/index.html
