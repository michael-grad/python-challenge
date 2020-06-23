# First we'll import the os module
# This will allow us to create file paths across operating systems
# gaol: read each line into a list
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


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
    
    count_months = 0
    net_total_amount = 0
    monthly_max_date = "Jan-2010"
    monthly_max_amount = 0
    monthly_min_date = "Jan-2010"
    monthly_min_amount = 0
    # Read each row of data after the header
    for row in csvreader:
        
        # print month-year 
        print(row[0])
        if int(row[1]) > monthly_max_amount:
            monthly_max_amount = int(row[1])
            monthly_max_date = row[0]
        if int(row[1]) < monthly_min_amount:
            monthly_min_amount = int(row[1])
            monthly_min_date = row[0]


        count_months = count_months + 1

        net_total_amount = net_total_amount + int(row[1])

    print("Financial Analysis")
    print("-----------------------------")    
    print(f"Total Months {count_months}")
    print(f"Total:  ${net_total_amount}")
    
    # AVERAGE_AMOUNT IS INCORRECT
    average_amount = net_total_amount / count_months
    # formatting code for average_amount sourced from https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
    print(f"Average Change:  {'{0:.2f}'.format(average_amount)}")
    
    print(f"Greatest Increase in Profits: {monthly_max_date} ({monthly_max_amount})")
    print(f"Greatest Decrease in Profits: {monthly_min_date} ({monthly_min_amount})")


# Specify the file to write to
output_path = os.path.join("analysis", "PyBank Summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])

    # Write the second row
    csvwriter.writerow(["-----------------------------"])

    # Write the third row
    csvwriter.writerow([f"Total Months {count_months}"])

    # Write the fourth row
    csvwriter.writerow([f"Total:  ${net_total_amount}"])

    # Write the fifth row
    csvwriter.writerow([f"Average Change:  {'{0:.2f}'.format(average_amount)}"])

    # Write the sixth row
    csvwriter.writerow([f"Greatest Increase in Profits: {monthly_max_date} ({monthly_max_amount})"])

    # Write the seventh row
    csvwriter.writerow([f"Greatest Decrease in Profits: {monthly_min_date} ({monthly_min_amount})"])

with open(csvpath) as csvfile:
    print(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = list(csv.reader(csvfile, delimiter=','))

print(csvreader)