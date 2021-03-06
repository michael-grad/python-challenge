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

    monthly_profit_losses = []
    profit_loss_difference = []

    # Read each row of data after the header
    for row in csvreader:
        
        # print month-year 
        # print(row[0])
        # Create a list of monthly profit losses
        monthly_profit_losses.append(row[1])
        
        # print(monthly_profit_losses)
        
        if int(row[1]) > monthly_max_amount:
            monthly_max_amount = int(row[1])
            monthly_max_date = row[0]
        if int(row[1]) < monthly_min_amount:
            monthly_min_amount = int(row[1])
            monthly_min_date = row[0]

        count_months = count_months + 1

        net_total_amount = net_total_amount + int(row[1])

# type(net_total_amount)
    # --------------------------------------
    # FIND AVERAGE AMOUNT OR PROFIT / LOSSES
    # --------------------------------------
    
    profit_loss_sum = 0
    monthly_difference = 0

    for i in range(1, len(monthly_profit_losses)):
        print(i,int(monthly_profit_losses[i]),int(monthly_profit_losses[i-1]))
        monthly_difference = int(monthly_profit_losses[i]) - int(monthly_profit_losses[i-1])
        profit_loss_sum += monthly_difference
    average_amount = profit_loss_sum / (len(monthly_profit_losses)-1)
    average_amount = '{0:.2f}'.format(average_amount)

    # Print Summary
    print(f"MONTHLY AVERAGE: {average_amount}")
    print("Financial Analysis")
    print("-----------------------------")    
    print(f"Total Months {count_months}")
    print(f"Total:  ${net_total_amount}")
    print(f"Average Change:  {average_amount}")
    print(f"Greatest Increase in Profits: {monthly_max_date} ({monthly_max_amount})")
    print(f"Greatest Decrease in Profits: {monthly_min_date} ({monthly_min_amount})")


# Specify the file to write to
output_path = os.path.join("analysis", "Financial Summary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
 #   csvwriter = csv.writer(csvfile, delimiter=',')

# writing to a txt file sourced from https://www.w3schools.com/python/python_file_write.asp
with open(output_path, 'w') as txtfile:

    # Write the first row (column headers)
    txtfile.write("Financial Analysis\n")

    # Write the second row
    txtfile.write("-----------------------------\n")

    # Write the third row
    txtfile.write(f"Total Months: {count_months}\n")

    # print(type(net_total_amount))
    # Write the fourth row
    txtfile.write(f"Total:  ${net_total_amount}\n")

    # Write the fifth row
    txtfile.write(f"Average Change:  {format(average_amount)}\n")

    # Write the sixth row
    txtfile.write(f"Greatest Increase in Profits: {monthly_max_date} ({monthly_max_amount})\n")

    # Write the seventh row
    txtfile.write(f"Greatest Decrease in Profits: {monthly_min_date} ({monthly_min_amount})\n")
