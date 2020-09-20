#Import os and csv modules
import os
import csv

employeeCSV = os.path.join("PyBoss", "employee_data.csv")

#Declare variables
empID = []
firstName = []
lastName = []
DOB = []
SSN = []
State = []
first = ""
last = ""

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

        #Assign second value in firstName[] to secondName[]
        last = firstName.pop()
        firstName.append(last[0])
        lastName.append(last[1])
    
#print(f"{empID}")
print(f"{firstName}")
print(f"{lastName}")