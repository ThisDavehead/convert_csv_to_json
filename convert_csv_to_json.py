"""
@author: David Adams
"""

import sys
import glob
import json
import csv

# First, a little trick to bypass the maxInt limitations for reading large csv files
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

# Path of csv input files.
input_path = 'PATH_TO_DIRECTORY_CONTAINING_CSV_FILES_USING_\\_SEPARATORS\\'
# Make an array of all csv files in the input path.
files = [f for f in glob.glob(input_path + "**/*.csv", recursive=True)]
# Path of json output files.
output_path = 'PATH_TO_TARGET_JSON_DIRECTORY_USING_\\_SEPARATORS\\'

# For each input file:
#   Make an output filename using the input filename with the extension changed to *.json.
#   Open both files for conversion of data.
for f in files:
    name, ext = f.split('.')
    name = name.split('\\')[-1]
    new_file = output_path + '{}.{}'.format(name, 'json')

    # Create list of dictionaries, with each dictionary being a row from the csv file
    with open(f, 'r', encoding='utf-8') as csv_input:
        reader = csv.DictReader(csv_input)
        rows = list(reader)

    # First clear the output file
    open(new_file).close()
    with open(new_file, 'w+', encoding='utf-8') as json_output:
        json.dump(rows, json_output)

print("done!")
