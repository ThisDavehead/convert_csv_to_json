"""
@author: David Adams
"""

import glob
import json
import io
import csv

# Path of csv input files.
input_path = 'PATH_TO_DIRECTORY_CONTAINING_JSONL_FILES_USING_\\_SEPARATORS\\'
# Make an array of all csv files in the input path.
files = [f for f in glob.glob(input_path + "**/*.csv", recursive=True)]
# Path of json output files.
output_path = 'PATH_TO_TARGET_CSV_DIRECTORY_USING_\\_SEPARATORS\\'

# For each input file:
#   Make an output filename using the input filename with the extension changed to *.json.
#   Open both files for conversion of data.
for f in files:
    name, ext = f.split('.')
    name = name.split('\\')[-1]
    new_file = output_path + '{}.{}'.format(name, 'json')
    data = {}
    with open(f, 'r', encoding='utf-8') as csv_input:
        csvReader = csv.DictReader(csv_input)
        # Each row should be a dictionary
        for rows in csvReader:

            # IMPORTANT: Change the following line's rows index to whichever
            # column acts as a unique identifier for the various rows
            key = rows['label']
            data[key] = rows
    with io.open(new_file, 'w', encoding="utf-8") as json_output_file:
        json_output_file.write(json.dumps(data, indent=4))
