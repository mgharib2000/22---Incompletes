"""
import csv

filename = "listNew.csv"

with open(filename, "r") as data:
    for line in csv.reader(data):
        print(line[1], line[0], "\n")

"""



"""
import csv

filename = "listNew.csv"

with open(filename, "r") as data:
    for line in csv.DictReader(data):
        print(line)

"""

"""
#List of dictionaries

from csv import DictReader

with open("listNew.csv", "r") as f:

    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)

    print(list_of_dict)
"""

import csv

with open("listOld.csv", "r") as t1, open("listNew.csv", "r") as t2:
    fileOne = t1.readlines()
    fileTwo = t2.readlines()

with open("listCompare.csv", "w") as outFile:
    for line in fileTwo:
        if line in fileOne:
            outFile.write(line)
