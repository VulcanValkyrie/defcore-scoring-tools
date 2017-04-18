#!/usr/bin/python3.5

import os
import argparse

# this script pulls the scorable capabilities from scoring.txt
# and used them to create a csv, which can be loaded into the
# spreadsheet tool of your choice for added convenience

# get args passed in
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", metavar='f', type=str,
                    action="store", dest="filename", default="scoring.csv")
result = parser.parse_args()
# now we get the filename for our new csv
if result.filename is None or not result.filename:
    filename = "scoring.csv"
else:
    filename = result.filename
# make sure our outfile exists and is empty
if os.path.exists(filename):
    os.remove(filename)
os.mknod(filename)
# open file
with open("scoring.txt") as read, open(filename, "a") as outfile:
    # first, print a header line to our file
    outfile.write(
        "capability name, widely deployed, used by tools, used by clients, future, complete, stable, discoverable, documented, required in last release, foundational, atomic, proximity, non-admin\n")
    # read in every line in the file
    for line in read:
        if ":" in line and "*" in line:
            # convert line to proper csv format
            # print(line)
            line = line.replace("] [", ",").replace("[", ",").replace("]*", "")
            line = line.split(",")[:-1]
            line = ",".join(line)
            line = " ".join(line.split())
            # print line to file
            outfile.write(line + "\n")
    # now close out our files
    outfile.close()
    read.close()
