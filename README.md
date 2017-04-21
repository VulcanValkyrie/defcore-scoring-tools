# defcore-scoring-tools

####################### Commit History & Progress ###########################

* 4/17/17
  - Initial commit. make-csv.py is in full working form, push-csv.py is still
    not at full functionality, although it shouldn't require too much work
* 4/19/17
  - fixed bugs concerning updating the scoring.txt file, as well as an
    alignment issue that broke score tabulation.
* 4/20/17
   - added functionality which allows you to run the script from the "tools"
     directory, rather than in the "working_materials" directory, which is,
     after all, the most appropriate location for a pair of scoring tools.

###################### Current Status & Functionality #######################

* make-csv.py
  - This is likely the final version of this script.
  - Its functionality is to pull all of the scorable lines in the scoring.txt
    file, and convert them to .csv format. This csv can then be imported into
    the user's spreadsheet tool of choice for greater ease of scoring.

* push-csv.py
  - Takes the csv you have modified, convert its format into that found in
    scoring.txt, and push all updated lines into the file.
