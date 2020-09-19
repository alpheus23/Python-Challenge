#Import the OS and CSV modules
import os
import csv

#Declare variables
monthTotal = 0
profitLosses = 0
changes = []
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
            
        change = int(row[1]) - next(int(row[1]))
        changes.append(change)
        print(changes)


    #Print out the Financial Analysis
    print(f"Total Months: {monthTotal}")
    print(f"Total: ${profitLosses}")