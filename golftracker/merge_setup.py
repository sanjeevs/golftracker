"""Script to merge the setup json values into other json files."""

import argparse
import os
import os.path
import json

from golftracker import tracker
def create_parser():
    """Create a command line parser."""
    parser = argparse.ArgumentParser(
        description="Merge the default values to json file(s)"
    )
    parser.add_argument(
        "--setup",
        "-s",
        default="",
        help="Setup json file for using default values",
    )
    parser.add_argument(
        "framedir", type=str, help="Filename or dir holding all the json files."
    )
    return parser

def merge_json(json_file, setup_file):
    with open(json_file) as json_fh:
        tracker_dict = json.load(json_fh)

    with open(setup_file) as setup_fh:
        setup_dict = json.load(setup_fh)

    for key in ["ball"]:
        if tracker_dict[key][0] == None:
            tracker_dict[key] = setup_dict[key]

    print(tracker_dict)
    #Overwrite the destination json file
    with open(json_file, "w") as json_fh:
        json.dump(tracker_dict, json_fh)


def main():
    """Main program"""
    opt = create_parser().parse_args()

    if os.path.isfile(opt.framedir):
        if opt.setup == "":
            raise ValueError(f"Need to provide the json setup file for merging")
        merge_json(opt.framedir, opt.setup)
    else:
        json_files = []

        for f in os.listdir(opt.framedir):
            split_tup = os.path.splitext(f)

            fname = os.path.join(opt.framedir, f)
            if os.path.isfile(fname) and split_tup[1] == ".json":
                json_files.append(fname)

        print(f">>Found {len(json_files)} frames to edit in dir '{opt.framedir}'")
        if opt.setup == "" and len(json_files) < 2:
            raise ValueError(f"Need to provide the json setup file for merging")
        else:
            if opt.setup:
                setup_json = opt.setup
            else:
                setup_json = json_files[0]
        print(f">>Using '{setup_json}' for merging into rest of json file")

        for f in json_files:
            merge_json(f, setup_json)