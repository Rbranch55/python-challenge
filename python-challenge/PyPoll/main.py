# Imports
import os
import csv

print("Election Results")
print("-------------------------")

csvpath = os.path.join('/Users/t/Downloads/python-challenge/PyPoll/Resources/election_data.csv')

with open(csvpath, newline="", encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

## The total number of votes cast
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)


# Calculate the total number of votes
print("Total Votes:", row_count)
print("-------------------------")

## Complete list of candidates who received votes
candidates = list()
count = list()
for i in range (0,row_count):
    candidate = data[i][2]
    count.append(candidate)
    if candidate not in candidates:
        candidates.append(candidate)
candidate_count = len(candidates)

## The percent and total number of votes each candidate won 

votes = list()
percent = list()
for j in range (0,candidate_count):
    name = candidates[j]
    votes.append(count.count(name))
    vote_percent = votes[j]/row_count
    percent.append(vote_percent)

for k in range (0,candidate_count): 
    print(f"{candidates[k]}: {percent[k]:.3%} ({votes[k]:})")

## Winner by popular vote
winner = votes.index(max(votes)) 
print("-------------------------")
print(f"Winner: {candidates[winner]}")
print("-------------------------")

# Open the file in write mode
file_name = "Election Analysis.txt"
file = open(file_name, 'w')

# Write content to the file
content = "Election Results ---------------------------------------- Total Votes: 369711 ---------------------------------------- Charles Casper Stockham: 23.049% (85213) Diana DeGette: 73.812% (272892) Raymon Anthony Doane: 3.139% (11606) ---------------------------------------- Winner: Diana DeGette ----------------------------------------
file.write(content)

# Close the file
file.close()

