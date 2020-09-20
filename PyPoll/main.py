#Import the OS and CSV modules
import os
import csv

#Declare variables
totalVotes = 0

khanVotes = 0
khanPercent = 0.0

correyVotes = 0
correyPercent = 0.0

liVotes = 0
liPercent = 0.0

tooleyVotes = 0
tooleyPercent = 0.0


#Create os path to reach csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Open CSV file
with open(csvpath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Skip over the first row of the csv file
    csvHeader = next(csvReader)

    for row in csvReader:
        totalVotes += 1
    


#Print out Election Results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVotes}")
print("---------------------------")
