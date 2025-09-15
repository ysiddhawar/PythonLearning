# quant/io.py
import csv  
#csv is the Python module (a toolbox for CSV files).
#import csv → we bring in Python’s built-in tool for handling CSV files.
import json  # import json → we bring in Python’s built-in tool for handling JSON files.
from typing import Dict  #from typing import Dict → this is a type hint helper. 
                         #Dict tells us: this variable will be a dictionary.
                         #It’s for readers and tools (not required by Python itself).

def save_summary_to_csv(summary: Dict, filename: str) -> None:

    #summary (the parameter) gets the value of summary
    #filename (the parameter) gets the string "summary.csv".
    #When we write -> None, it is a type hint that says:
    #"This function does not give anything back, it only does some work (like saving a file)."
    """
    summary: dict mapping strategy_name -> report dict #Explains that summary is a dict
    filename: path to write CSV  #filename is where to save, e.g. "summary.csv"
    """
    # CSV header order
    header = ["strategy", "total_pnl", "wins", "losses", "total_trades", "win_rate", "avg_pnl"]

    #Think of it like writing the labels for the top row of an Excel sheet 
    # That very first row is called the header because it describes what each column means. 
    # So here header is just a list that holds those labels, in order.

    with open(filename, "w", newline="") as f:
        #with ...: → ensures file will close automatically after block ends.
        #open a file to write ("w" = write). 
        # newline="" avoids extra blank lines in CSV on Windows.
        # as f → call this open file f (a variable).

        writer = csv.writer(f)
        #csv.writer(...) is a function inside that toolbox called csv(Python module)
        #It takes a file (here f, which we opened earlier) and builds a writer object.

        writer.writerow(header)
        #👉 writer.writerow(header) writes one row to the CSV file with all those values 
        # separated by commas.
        #Here we’re writing the first row = the header row (the column labels).
        for name, report in summary.items():
            writer.writerow([
                name,
                report["total_pnl"],
                report["wins"],
                report["losses"],
                report["total_trades"],
                report["win_rate"],
                report["avg_pnl"],
            ])
            #For each strategy, write a row with:
            #name (the strategy name string)
            #and all the values (total_pnl, wins, etc).

def save_summary_to_json(summary: Dict, filename: str) -> None:
    """
    Save the summary dictionary as JSON (human-readable with indent=2)
    """
    with open(filename, "w") as f:
        json.dump(summary, f, indent=2)
        #json.dump(summary, f, indent=2) → write the dictionary summary into the file, 
        # formatted with indentation 2 spaces (makes it pretty).
