#!/usr/bin/python3.5

import argparse
import fileinput
import os
import subprocess

# this script takes the scored capabilities from scoring.csv
# and pushes them back to the original scoring doc. It then
# runs tabulate-scores.py for added convenience

#first we need to get the base path of the defcore directory
path = os.path.dirname(os.path.abspath(__file__))
path = path.split("defcore")[0] + "defcore/working_materials"
#get args passed in
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", metavar='f', type=str, action="store", dest="filename", default="scoring.csv")
result = parser.parse_args()
#create an empty tempfile for us to work with
if os.path.exists(path + "/temp.txt"):
    os.remove(path + "/temp.txt")
os.mknod(path + "/temp.txt")
#now get the name of the csv file we will be using to update scoring.txt
if result.filename is None or not result.filename:
    filename = path + "/scoring.csv"
else:
    filename = "/" + result.filename
#open the file we will be reading from
with open(path + filename) as read, open(path + "/scoring.txt") as oldfile, open(path +"/temp.txt", "w") as outfile:
    for oldline in oldfile:
        status = 0
        if "] [" in oldline and ":" in oldline and "-" in oldline:
            for line in read:
                capability = line.split(":")[0].rstrip().lstrip()
                line = line.split(",")
                #reformat csv entry
                line = "[" + ",".join(line[1:4])+"] ["+ ",".join(line[4:7])+"] ["+",".join(line[7:10])+"] ["+",".join(line[10:13]) + "] [" +line[-1].replace("\n", "")+ "] [0]*".lstrip()
                oldcap = oldline.split(":")[0].rstrip().lstrip()
                if oldcap == capability:
                    capability = capability + ":"
                    line = capability.ljust(35, " ") + line.rstrip().rjust(55, " ") + "\n"
                    outfile.write(line)
                    status = 1
                    break
            read.seek(0)
        if status == 0:
            if not "] [" in oldline and not ":" in oldline:
                outfile.write(oldline)
            else:
                print(oldline + " not found in the updated scoring")
    os.rename(path + "/temp.txt", path + "/scoring.txt")
    read.close(); oldfile.close(); outfile.close()
subprocess.run([path + "/tabulate_scores.py", "-s", path + "/scoring.txt", "-c", path + "/tabulated_scores.csv"])
