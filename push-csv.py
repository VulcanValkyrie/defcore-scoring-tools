#!/usr/bin/python3.5

import argparse
import fileinput
import os

# this script takes the scored capabilities from scoring.csv
# and pushes them back to the original scoring doc. It then
# runs tabulate-scores.py for added convenience

# get args passed in
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", metavar='f', type=str,
                    action="store", dest="filename", default="scoring.csv")
result = parser.parse_args()
# create an empty tempfile for us to work with
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
os.mknod("temp.txt")
# now get the name of the csv file we will be using to update scoring.txt
if result.filename is None or not result.filename:
    filename = "scoring.csv"
else:
    filename = result.filename
# open the file we will be reading from
with open(filename) as read, open("scoring.txt") as oldfile, open("temp.txt", "w") as outfile:
    for oldline in oldfile:
        status = 0
        if "] [" in oldline and ":" in oldline and "-" in oldline:
            for line in read:
                capability = line.split(":")[0].rstrip()
                line = line.split(",")
                # reformat csv entry
                line = "[" + ",".join(line[1:4]) + "] [" + ",".join(line[4:7]) + "] [" + ",".join(
                    line[7:10]) + "] [" + ",".join(line[10:13]) + "] [" + line[-1].replace("\n", "") + "] [0]*".lstrip()
                oldcap = oldline.split(":")[0].rstrip()
                # oldscore = oldline.split(":")[0].rstrip().split("[", 2)[0]
                # score = line.split("[", 2)[0]
                if oldcap == capability and line != oldline:  # and score != oldscore:
                    line = capability.rjust(
                        35, " ") + ":" + line.rstrip().rjust(55, " ") + "\n"
                    outfile.write(line)
                    status = 1
                    break
            read.seek(0)
        if status == 0:
            if "] [" in oldline and ":" in oldline and "-" in oldline:
                oldcap = oldline.split(":")[0].rstrip()
                oldline = oldline.split(":")[-1].lstrip()
                oldline = oldcap.rjust(
                    35, " ") + ":" + oldline.rstrip().rjust(55, " ") + "\n"
                outfile.write(oldline)
            else:
                outfile.write(oldline)
    os.rename("temp.txt", "scoring.txt")
    read.close()
    oldfile.close()
    outfile.close()
