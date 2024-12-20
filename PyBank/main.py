import os
import csv

# Set relative path for csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    # Store the header row
    header = next(reader)
    print("Header Row:", header)

    # Define variables to track the financial data
    count = 0
    total = 0
    prev_profit = 0
    net_change_list = []
    month_of_change = []
    total_change = 0
    
    # Process each row of data
    for row in reader:
        count += 1
        current_profit = int(row[1])
        total += current_profit
        
        if prev_profit != 0:
            profit_change = current_profit - prev_profit
            net_change_list.append(profit_change)
            month_of_change.append(row[0])
            total_change += profit_change
            
        prev_profit = current_profit
    
    avg_change = total_change / (count - 1)
    
    max_increase = max(net_change_list)
    max_increase_month = month_of_change[net_change_list.index(max_increase)]
  
    max_decrease = min(net_change_list)
    max_decrease_month = month_of_change[net_change_list.index(max_decrease)]

    # Print Results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")
