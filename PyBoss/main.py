#Import os and csv modules
import os
import csv

employeeCSV = os.path.join("PyBoss", "employee_data.csv")

#Declare variables
empID = []

firstName = []
first = ""

lastName = []
last = ""

DOB = []
date = ""
month = ""
day = ""
year = ""

SSN = []
State = []


#Open CSV file
with open(employeeCSV) as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")

    #Skip over the first row of the csv file
    csvHeader = next(csvReader)

    #Read through each row and assign appropriate data to appropriate list
    for row in csvReader:
        #Add Employee ID
        empID.append(row[0])

        #Split name value into first and last
        first = row[1]
        firstName.append(first.split())

        #Break name row into a two index list with the first and last name in different indexes
        last = firstName.pop()

        #Assign value at index[0] to firstName and value at index[1] to lastName
        firstName.append(last[0])
        lastName.append(last[1])

        #Split date value by using "-" as the seperator
        date = row[2]
        date.split("-")
        print(f"{date}")

#print(f"{empID}")
#print(f"{firstName}")
#print(f"{lastName}")
#print(f"{DOB}")