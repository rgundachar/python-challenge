import os as os
import csv as csv
csvpath = os.path.join('.', 'resources', 'budget_data.csv')
total = 0
revenue = []
date = []
rev_change = []
avg_rev_change = 0
max_rev_change = 0
min_rev_change = 0
min_rev_change_date = 0
max_rev_change_date = 0

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # total
    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total : $", sum(revenue))
    for i in range(1, len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])
    print("Average Change: $", round(avg_rev_change))
    print("Greatest Increase in Profits:", max_rev_change_date, "($", max_rev_change, ")")
    print("Greatest Decrease in Profits:", min_rev_change_date, "($", min_rev_change, ")")



