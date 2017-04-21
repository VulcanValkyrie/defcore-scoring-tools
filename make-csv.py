#!/usr/bin/python3.5

import os
import argparse

# this script pulls the scorable capabilities from scoring.txt
# and used them to create a csv, which can be loaded into the
# spreadsheet tool of your choice for added convenience

#first, get the path of the dir we need to be adding into
path = os.path.dirname(os.path.abspath(__file__))
path = path.split("defcore")[0] + "defcore/working_materials"
#get args passed in
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", metavar='f', type=str, action="store", dest="filename", default="scoring.csv")
result = parser.parse_args()
# now we get the filename for our new csv
if result.filename is None or not result.filename:
    filename = "/scoring.csv"
else:
    filename = "/" + result.filename

# make sure our outfile exists and is empty
if os.path.exists(path + filename, '0751'):
    os.remove(path + filename, 751)
os.mknod(path + filename)
# open file
with open(path + "/scoring.txt") as read, open(path + filename, "a") as outfile:
    # first, print a header line to our file
    outfile.write("capability name, widely deployed, used by tools, used by clients, future, complete, stable, discoverable, documented, required in last release, foundational, atomic, proximity, non-admin\n")
    # read in every line in the file
    for line in read:
        if ":" in line and "*" in line:
            # convert line to proper csv format
            line = line.replace("] [", ",").replace("[", ",").replace("]*", "")
            line = line.split(",")[:-1]
            line = ",".join(line)
            line = " ".join(line.split())
            # print line to file
            outfile.write(line + "\n")
    # now close out our files
    outfile.close(); read.close()
