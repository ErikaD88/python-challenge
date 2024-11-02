# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  
file_to_output = os.path.join("analysis", "budget_analysis.txt")  

# Define variables to track the financial data
total_months = 0
total_net = 0
profit_losses = []
months = []
previous_profit = None
net_change_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        month = row[0]  # Get the month
        profit_loss = int(row[1])  # Convert profit/loss to integer
        
        total_months += 1  # Increment total month count
        total_net += profit_loss  # Sum the profit/loss
        profit_losses.append(profit_loss)  # Record profit/loss value
        months.append(month)  # Record month
        
        # Calculate the net change and store it
        if previous_profit is not None:
            net_change = profit_loss - previous_profit  # Calculate change
            net_change_list.append(net_change)  # Store the change

        previous_profit = profit_loss  # Update previous profit
       
# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Calculate the greatest increase and decrease in profits (month and amount)
greatest_increase = max(net_change_list) if net_change_list else 0
greatest_decrease = min(net_change_list) if net_change_list else 0

# Getting the dates for the corresponding greatest changes
greatest_increase_index = net_change_list.index(greatest_increase) if greatest_increase in net_change_list else -1
greatest_decrease_index = net_change_list.index(greatest_decrease) if greatest_decrease in net_change_list else -1

# Use the index to find the corresponding month for increase/decrease
greatest_increase_date = months[greatest_increase_index + 1] if greatest_increase_index != -1 else ""
greatest_decrease_date = months[greatest_decrease_index + 1] if greatest_decrease_index != -1 else ""

# Generate the output summary
output = (
    f"""Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${total_net}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
    Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"""
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)