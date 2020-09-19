#Import the OS and CSV modules
import os
import csv

#Declare variables
monthTotal = 0
profitLosses = 0
changes = []
difference = 0.0
differences = []
averageChange = 0.0

#Create os path to reach csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Open CSV file
with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    #Skip over the first row of the csv file
    csvHeader = next(csvReader)

    #Read through each row of data after header
    for row in csvReader:
        monthTotal += 1
        profitLosses += int(row[1])
            
        change = int(row[1])
        changes.append(change)


    n = 0
    j = 1
    for values in changes:
        difference = (int(changes[n]) - int(changes[j]))
        differences.append(difference)
        n += 1
        j += 1
        if j > 85:
            break

    print(differences)
    averageChange = sum(differences) / len(differences)


    #Print out the Financial Analysis
    print(f"Total Months: {monthTotal}")
    print(f"Total: ${profitLosses}")
    print(f"Average Change: ${averageChange:.2f}")