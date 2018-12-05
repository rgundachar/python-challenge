import os as os
import csv as csv
from collections import Counter
csvpath = os.path.join('.', 'resources', 'election_data.csv')
votes = []
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # total
    for row in csvreader:
        votes.append(row[0])
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", len(votes))
    print("-----------------------------------")

result = {}
Names = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvreader:
        if row[2] not in Names:
            Names.append(row[2])

with open(csvpath, newline='') as csvfile:
    next(csvfile)
    occurrence = Counter((row[2]) for row in csv.reader(csvfile))
maxVotes = 0
file = open("testfile.txt", "w")

for cnt in Names:
    print(cnt, ":",  occurrence[cnt]/len(votes)*100, " (", occurrence[cnt], ")")
    if occurrence[cnt]/len(votes)*100 > maxVotes:
        maxVotesName = cnt
        maxVotes = occurrence[cnt]/len(votes)*100
print("-----------------------------------")
print("Winner :", maxVotesName)
print("-----------------------------------")

file.write("Winner :" + maxVotesName)
