import csv
import os


EL = os.path.join("..","Homework 3", "PyPoll","Election_Data.csv")
with open(EL) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    print("Hola Mundo")

    TKhan       = 0
    TCorrey     = 0
    TLi         = 0
    TOtooley    = 0

    print("Hola Mundo")

    for row in csvreader:
            Elist = str (row[2])
            if Elist == "Khan":
                TKhan += 1
            elif Elist == "Correy":
                TCorrey += 1
            elif Elist == "Li":
                TLi += 1
            elif Elist == "O'Tooley":
                TOtooley += 1

TVotes = TKhan + TCorrey + TLi + TOtooley

print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {TVotes} ")
print("---------------------------------------")
print(f"Khan:{TKhan} " + f"{TKhan/TVotes}%")
print(f"Correy:{TCorrey} " + f"{TCorrey/TVotes}%")
print(f"Li:{TLi} " + f"{TLi/TVotes}%")
print(f"O´Tooley:{TOtooley}" + f"{TOtooley/TVotes}%")



