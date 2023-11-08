# Golf Swing Capture

Create a database with all the information about the golf swing.

## Flowchart to create the database
Refer to ![FlowChart1](/docs/source/images/golfswing_capture.svg) for the steps.

Here's how the flowchart works:

The process starts by running the create_swing_db script.
Inside the create_swing_db script, there's a check to see if the pose was detected. If yes, it creates a pickle database and the process ends.

```
create_swing_db <video_fname>
```

If no pose is detected, the flow moves to the manual labeling of golf poses using the label_golf_poses script.
Then, the user selects the starting and ending poses via the GUI provided by the script.
Afterward, a CSV file with the pose data is created.

```
label_golf_poses <video_fname>
```

The model is then trained with the new CSV file using the train_posemodel script.
Following the training, the create_swing_db script is run again to create the pickle database with the updated model.


The process ends after the pickle database is successfully created.

## Manual Creation
The above flow is not yet working. Hence a manual process can be used to populate the database with the club head
position.

```
label_club_head <pkl_database>
```

The intent is that using the manual label and some optical algorithms the club head position can be created for each
frame.

To adjust the algorithms parameters use the helper script.

```
tune_line_det <pkl_database>
```

To see the result of the process use the helper script below.

```
track_golf_club <pkl_database>
```

