import csv
import os
import statistics

BK = os.path.join("..","Homework 3","PyBank","PyBank_Data.csv")
with open(BK) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    next(csvfile)
    Contador=[]
    Total = 0
    
    for row in csvreader:
        Contador.append(int(row[1]))   
        if max (Contador)==row[1]:            
                R0=(str (row[0]))
    
TotalMonths = len(row[0])
Total += int(row[1])

print ("Financial Analysis")
print ("----------------------------------")
print (f"Total Months: {TotalMonths}")
print (f"Total: {Total}")
print (f"Average Change:")
print(f"Greatest increase in profits:($ {max (Contador)})")
print(f"Greatest decrease in profits:($ {min (Contador)})")
# print(f"{R0}")
