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

popularVote = []
winner = ""


#Create os path to reach csv file
csvpath = os.path.join("Resources", "election_data.csv")

#Open CSV file
with open(csvpath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Skip over the first row of the csv file
    csvHeader = next(csvReader)

    #Loop through each row and add counters to candidate votes based on values in row[2]
    for row in csvReader:
        totalVotes += 1

        if row[2] == "Khan":
            khanVotes += 1

        elif row[2] == "Correy":
            correyVotes += 1

        elif row[2] == "Li":
            liVotes += 1

        elif row[2] == "O'Tooley":
            tooleyVotes += 1

#Calculate percentage of votes each candidate received
khanPercent = (khanVotes / totalVotes) * 100
correyPercent = (correyVotes / totalVotes) * 100
liPercent = (liVotes / totalVotes) * 100
tooleyPercent = (tooleyVotes / totalVotes) * 100

#Put all vote counter into an array for later manipulation
popularVote = [khanVotes, correyVotes, liVotes, tooleyVotes]

#Ifelse statement to determine which variable has highest value, and assign corresponding candidate to winner
if khanVotes == max(popularVote):
    winner = "Khan"

elif correyVotes == max(popularVote):
    winner = "Correy"

elif liVotes == max(popularVote):
    winner = "Li"

elif tooleyVotes == max(popularVote):
    winner = "O'Tooley"

#Print out Election Results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVotes}")
print("---------------------------")
print(f"Khan: {khanPercent:.2f}% ({khanVotes})")
print(f"Correy: {correyPercent:.2f}% ({correyVotes})")
print(f"Li: {liPercent:.2f}% ({liVotes})")
print(f"O'Tooley: {tooleyPercent:.2f}% ({tooleyVotes})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#Specify the file to write to  
outputPath = os.path.join("Analysis", "analysis.txt")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(outputPath, 'w') as txtFile:

    #Recreate Election Results as a single print statement to be pushed to txt file
    outputTxt = ("Election Results\n"
                "---------------------------\n"
                f"Total Votes: {totalVotes}\n"
                "---------------------------\n"
                f"Khan: {khanPercent:.2f}% ({khanVotes})\n"
                f"Correy: {correyPercent:.2f}% ({correyVotes})\n"
                f"Li: {liPercent:.2f}% ({liVotes})\n"
                f"O'Tooley: {tooleyPercent:.2f}% ({tooleyVotes})\n"
                "---------------------------\n"
                f"Winner: {winner}\n"
                "---------------------------")
    txtFile.write(outputTxt)
