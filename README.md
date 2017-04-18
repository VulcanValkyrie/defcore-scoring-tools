# defcore-scoring-tools

####################### Commit History & Progress ###########################

* 4/17/17
  - Initial commit. make-csv.py is in full working form, push-csv.py is still
    not at full functionality, although it shouldn't require too much work


###################### Current Status & Functionality #######################

* make-csv.py
  - This is likely the final version of this script.
  - Its functionality is to pull all of the scorable lines in the scoring.txt
    file, and convert them to .csv format. This csv can then be imported into
    the user's spreadsheet tool of choice for greater ease of scoring.

* push-csv.py
  - This is not a complete script, though it shouldn't take too long to
    straighten out
  - Its functionality will be to take the csv you have modified, convert
    its format into that found in scoring.txt, and push all updated lines
    into the file.
  - I may just have the script run scoring.txt, given that the conversion
    process renders the original scores incorrect.
