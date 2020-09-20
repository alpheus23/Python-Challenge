#Import the OS and CSV modules
import os
import csv

#Imports numpy modules to search through arrays for specific values
import numpy as np

#Declare variables
monthTotal = 0
profitLosses = 0
changes = []
months = []
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

    #Read through each row of data after header and increase month total count and profit/losses each time it is looped through
    for row in csvReader:
        monthTotal += 1
        profitLosses += int(row[1])
            
        #Take the profit value and put it into an array for later manipulation
        change = int(row[1])
        changes.append(change)

        #Take the month value and put it into an array for later manipulation
        month = row[0]
        months.append(month)

    #Declare variables to look through values in changes array
    n = 0
    j = 1

    #Loop through the values of the changes array to determine the difference between an index and the index ahead of it
    for values in changes:
        difference = (int(changes[j]) - int(changes[n]))
        differences.append(difference)

        #Increase n and j counters to calculate the difference between the next values in the array at the specified indexes
        n += 1
        j += 1

        #Prevents list index out of range error
        if j > 85:
            break

    #Find the index where the Greatest Increase in Profits is stored
    maxDiffIndex = differences.index(max(differences))

    #Find the index where the Greatest Decrease in Profits is stored
    minDiffIndex = differences.index(min(differences))

    #print(differences)
    #Calculate the average of the changes in Profit/Losses
    averageChange = sum(differences) / len(differences)

    #Print out the Financial Analysis
    print(f"Total Months: {monthTotal}")
    print(f"Total: ${profitLosses}")
    print(f"Average Change: ${averageChange:.2f}")
    print(f"Greatest Increase in Profits: {months[maxDiffIndex + 1]} ${max(differences)}")
    print(f"Greatest Decrease in Profits: {months[minDiffIndex + 1]} ${min(differences)}")