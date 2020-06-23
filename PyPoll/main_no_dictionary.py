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
    khan_count = 0
    khan_percent = 0
    correy_count = 0
    correy_percent = 0
    li_count = 0
    li_percent = 0
    o_tooley_count = 0
    o_tooley_percent = 0
    
    for row in csvreader:
        
        if row[2] == "Khan":
            khan_count = khan_count + 1
        if row[2] == "Correy":
            correy_count = correy_count + 1
        if row[2] == "Li":
            li_count = li_count + 1
        if row[2] == "O\'Tooley":
            o_tooley_count = o_tooley_count + 1
            
        # print(row[2])

        total_votes = total_votes + 1

    winner = "khan"
    # percent formatting code source from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
    khan_percent = '{0:.3%}'.format(khan_count / total_votes)
    correy_percent = '{0:.3%}'.format(correy_count / total_votes)
    li_percent = '{0:.3%}'.format(li_count / total_votes)
    o_tooley_percent = '{0:.3%}'.format(o_tooley_count / total_votes)

    # Define Winner
    if khan_percent > correy_percent and khan_percent > li_percent and khan_percent > o_tooley_percent:
        winner = "Khan"
    if correy_percent > khan_percent and correy_percent > li_percent and correy_percent > o_tooley_percent:
        winner = "Correy"
    if li_percent > khan_percent and li_percent > correy_percent and li_percent > o_tooley_percent:
        winner = "Li"
    if o_tooley_percent > khan_percent and o_tooley_percent > correy_percent and o_tooley_percent > li_percent:
        winner = "O'Tooley"

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:  {total_votes}")
    print(f"Khan: {khan_percent} ({khan_count})")
    print(f"Correy: {correy_percent} ({correy_count})")
    print(f"Li: {li_percent} ({li_count})")
    print(f"O'Tooley: {o_tooley_percent} ({o_tooley_count})")
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

    # Write the third row
    csvwriter.writerow([f"Total Votes:  {total_votes}"])

    # Write the fourth row
    csvwriter.writerow([f"Khan: {khan_percent} ({khan_count})"])

    # Write the fifth row
    csvwriter.writerow([f"Correy: {correy_percent} ({correy_count})"])

    # Write the sixth row
    csvwriter.writerow([f"Li: {li_percent} ({li_count})"])

    # Write the seventh row
    csvwriter.writerow([f"O'Tooley: {o_tooley_percent} ({o_tooley_count})"])

    # Write the eighth row
    csvwriter.writerow(["-----------------------------"])

    # Write the nineth row
    csvwriter.writerow([f"Winner:  {winner}"])

    # Write the tenth row
    csvwriter.writerow(["-----------------------------"])