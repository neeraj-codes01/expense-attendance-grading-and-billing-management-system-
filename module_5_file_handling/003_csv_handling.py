import csv
import pandas as pd
with open("students.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["name"] ,row["marks"])
        