Introduction
==============
This package detects the various elements in a golf swing. It does this by tracking various points in the swing and outputing it into a json file.

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
    "width" : 1024,
    "height" : 900,
	"ball": [1, 2],
	"shaft": [10, 20, 30, 40]
}
```

   