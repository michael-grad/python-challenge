# First we'll import the os module
# This will allow us to create file paths across operating systems
# gaol: read each line into a list
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')


# Reading using CSV module
print("opening", csvpath)
with open(csvpath) as csvfile:
    print(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    # next pops off the first line off
    csv_header = next(csvreader)
    print("csv_header is a ", type(csv_header))
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    total_votes = 0
    candidate_list = []
    # khan_count = 0
    # khan_percent = 0
    # correy_count = 0
    # correy_percent = 0
    # li_count = 0
    # li_percent = 0
    # o_tooley_count = 0
    # o_tooley_percent = 0
    
    candidate_totals = {}
    for row in csvreader:
        
        # Code for lookup of key in dictionary sourced from https://www.educative.io/edpresso/how-to-check-if-a-key-exists-in-a-python-dictionary
        if row[2] not in candidate_totals:
            candidate_totals[row[2]] = 1

        else:
            candidate_totals[row[2]] = candidate_totals[row[2]] + 1
                
                 
        # print(row[2])

        total_votes = total_votes + 1

    # print(candidate_totals)
    # winner = "khan"

    # khan_count = candidate_totals.get("Kahn")
    # print(khan_count)

    # --------------------------------------------
    # CREATE A DICTIONARY OF CANDIDATE PERCENTAGES
    # --------------------------------------------
    candidate_percents = {}

    # code for counting keys is sourced from https://stackoverflow.com/questions/2212433/counting-the-number-of-keywords-in-a-dictionary-in-python
    number_of_candidates = len(candidate_totals.keys())
    # print("Type:  ", type(number_of_candidates))
    # print(f"No of candidates:  {number_of_candidates}")
    
    # Populate keys and values for dictionary candidate_percents
    i=0
    
    # DEBUGGED - CODE BREAKS HERE - WHY???
    for key in candidate_totals:

        # get method sourced from https://www.tutorialspoint.com/python/dictionary_get.htm
        candidate_percents[key] = '{0:.3%}'.format(int(candidate_totals.get(key)) / total_votes)
        # print(candidate_percents)
        # print(candidate_totals)
        

    # --------------------------------------------
    # IDENTIFY THE WINNER BY COMPARING PERCENTAGES
    # --------------------------------------------

    # Looping through a dictionary by an index sourced from https://stackoverflow.com/questions/17793364/python-iterate-dictionary-by-index
    i=0
    j = 0
    
    # Sorting code sourced from https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
    sorted_candidate_totals = sorted(candidate_totals.items(), key=lambda x: x[1], reverse=True)
    sorted_candidate_percents = sorted(candidate_percents.items(), key=lambda x: x[1], reverse=True)
    winner = list(candidate_totals)[0]
    # print("Sorted",sorted_candidate_totals)
    # print("Sorted",sorted_candidate_percents)
    # print('Winner : ',winner)
    
    # percent formatting code source from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
    # khan_percent = '{0:.3%}'.format(khan_count / total_votes)
    # correy_percent = '{0:.3%}'.format(correy_count / total_votes)
    # li_percent = '{0:.3%}'.format(li_count / total_votes)
    # o_tooley_percent = '{0:.3%}'.format(o_tooley_count / total_votes)

    # ----------------------
    # # PRINT ELECTION RESULTS
    # ----------------------

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:  {total_votes}")
    
    # Make a list of dictionaires sorted_candidate_percents and sorted_candidawte_totals
    candidate_stats = [sorted_candidate_percents,sorted_candidate_totals]
    candidate_list = list(candidate_totals)
    # print(candidate_list)
    # Printing key of candidate_totals sourced from https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-65.php
    # Printing values from dictionary sourced from 
    # NOT WORKING - How to get retrieve values from a dictionary by using the index
    for candidate in candidate_list:
        print(f"{candidate}:  {candidate_percents[candidate]} ({candidate_totals[candidate]})")
            
    print("-------------------------")
    print(f"Winner:  {winner}")
    print("-------------------------")

    # Specify the file to write to
output_path = os.path.join("analysis", "PyPoll Summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])

    # Write the second row
    csvwriter.writerow(["-----------------------------"])

    # Write candidate, candidate percent, and (candidate total)
    for candidate in candidate_list:
        csvwriter.writerow([f"{candidate}:  {candidate_percents[candidate]} ({candidate_totals[candidate]})"])

    # Write the eighth row
    csvwriter.writerow(["-----------------------------"])

    # Write the nineth row
    csvwriter.writerow([f"Winner:  {winner}"])

    # Write the tenth row
    csvwriter.writerow(["-----------------------------"])