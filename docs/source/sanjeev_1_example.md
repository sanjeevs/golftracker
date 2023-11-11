# Introduction
This is an example of using the software to analyze my swing.

## Installation

Assume that you have downloaded the software using pip.

## Download

Pleaase download the test video from [GoogleDrive](https://drive.google.com/file/d/1oMrw_s38yRlgSvNYwby3CzHN6u5yqmND/view?usp=sharing) into a folder say "test1".

## Capture Golf Swing

Run the command to create the capture database.

```
create_swing_db dwn_rh_sanjeev_1.mov
```

This should create the pickle database "dwn_rh_sanjeev_1.pkl"

## Visualize Golf Swing

Run the command to visualize the swing.

```
display_golf_swing dwn_rh_sanjeev_1.pkl
```

## Analyze Golf Swing

Run the command to analyze the swing.

```
analyze_golf_swing dwn_rh_sanjeev_1.pkl
```
