.. _arch_doc:

Overview
=========
The major objects involved are

* GolfSwing
    Aggregate root that stores the results of the operations.

* Media Pipe Operation
    Service that processes the video frames and writes the results to golfswing

* ML Pose Operation
    Service that runs the ml model on each frame and classifies the various poses in the swing.

* Club Position
    This runs cv2 algorithm to compute the golf club in each frame.

GolfSwing
-----------
Contains the following data structures for storage.

* Media Pipe Landmarks
    Media pipe results are stored in value class GolfData. It stores landmarks for each frame in a list.

* Golf Pose Results
    The ml model results are stored in value class GolfPoses. This stores the pose and the prob as a tuple in 
    an associative array indexed by frame number.


* Club positon
    The golf club is represented as a tuple of 2 points to make a line. It is stored as a tuple in an associative
    array indexed by frame number.


