import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  
file_to_output = os.path.join("analysis", "election_analysis.txt")  

# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  

    for row in csvreader:
        total_votes += 1  
        candidate = row[2]  

        if candidate in candidates:
            candidates[candidate] += 1 
        else:
            candidates[candidate] = 1  

# Calculate percentage of votes and determine the winner
percentage_per_candidate = {}
for candidate, votes in candidates.items():
    percentage_per_candidate[candidate] = (votes / total_votes) * 100

# Find the winner
winner = max(candidates, key=candidates.get)

# Prepare output
output_lines = []
output_lines.append(f'Election Results')
output_lines.append(f'-------------------------')
output_lines.append(f'Total Votes: {total_votes}')
output_lines.append(f'-------------------------')

for candidate, votes in candidates.items():
    percentage = percentage_per_candidate[candidate]
    output_lines.append(f'{candidate}: {percentage:.3f}% ({votes})')

output_lines.append(f'-------------------------')
output_lines.append(f'Winner: {winner}')
output_lines.append(f'-------------------------')

# Print the results to the terminal
for line in output_lines:
    print(line)

# Exporting to text file
output_file = os.path.join('Analysis', 'pyPoll_output.txt')
pyPolloutput = open(output_file, "w")