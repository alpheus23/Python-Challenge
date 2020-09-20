#Import os and csv modules
import os
import csv

employeeCSV = os.path.join("PyBoss", "employee_data.csv")

#Lists to store data
empID = []
firstName = []
lastName = []
DOB = []
SSN = []
State = []

#Open CSV file
with open(employeeCSV) as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")

    #Skip over the first row of the csv file
    csvHeader = next(csvReader)

    #Read through each row and assign appropriate data to appropriate list
    for row in csvReader:
        empID.append(row[0])
    
print(f"{empID}")