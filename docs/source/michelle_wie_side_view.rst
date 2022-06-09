Example: MichelleWei Side View
==============================
To follow this example you would need to install helper package `spvideoutils <https://pypi.org/project/spvideoutils>`_


Steps
---------
#. Download the side view of the golf swing by Michelle Wei from `YouTube <https://www.youtube.com/watch?v=6LuiISfKa3o>`_

#. Split the video mp4 into frames using *video_split*.

#. Manually select the tracker using *golfeditor*.

#. Convert tracker json to png using *modelview*.

#. Create output video using *video_merge*.

Example Commands
-----------------
Assume file downloaded is test1.mp4. Use the first frame in *golfeditor* to mark the static trackers. ::

   video_split test1.mp4    // Creates ouptut dir test1 with frames
   golfeditor test1         // select tracker in each frame and create json.
   merge_setup test1        // Fill json files with static info.
   modelview test1          // Convert json to png files.
   video_merge test1        // Convert png files to mp4 file 'merge.mp4'

