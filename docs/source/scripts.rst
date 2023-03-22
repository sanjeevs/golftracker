.. _scripts_doc:

Scripts
========
List of scripts provided in the package.

Primary Scripts
----------------

The package provides a list of scripts in **scripts** directory that aid in this.


* resize_in_video 

  This script resizes, rotates, crops the input video to create a video suitable for analysis.
* **create_swing_db**

  This is the main script that reads in the video and creates a pickle database for post engine analysis.
* **display_golf_swing**

  This displays the pickle database with the various processing stages videos.
* info_swing_db

  This scripts dumps the information stored  in the pickle database. Useful for debug.

* label_club_head

  This script is used by user to label the club head in the video. Provides help to detect it in video.

* label_golf_poses
  
  This scripts is used by the user to label the various golf poses. Used to train the ai engine.


Helper Scripts
----------------
These scripts in the *utils* directory are used for development.

* create_posemodel.py

  Creates the pose ml model from scratch.

* train_posemodel

  This script is used for training the above model.

* predict_posemodel

  Run the ml model through the video.