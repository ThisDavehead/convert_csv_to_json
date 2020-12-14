# convert_csv_to_json
Convert multiple *.csv files to *.json files.

Note: This script was written with my Windows environment in mind.  

How to use:  
1) Edit this script's input path to where all your csv files are.  
2) Edit this script's output path to where you want all your json files to go.  
3) Make sure the separators used in the path names match the separator used in the name.split expression (line 35). I used '\\\\'.  
4) Run 'python convert_csv_to_json.py'  
5) Your files should be converted relatively quickly. It only took me a few minutes to convert 15 csv files (8GB total).  


Each .csv file will have a corresponding .json file written for it. For example:  

Input Directory:  
    ex1.csv  
    ex2.csv  
    ex3.csv  

Output Directory (after running):  
    ex1.json  
    ex2.json  
    ex3.json  


Each json file's format will be a list of dictionaries, with each dictionary representing a row from the corresponding csv file. The dictionaries' keys should have double quotes.
