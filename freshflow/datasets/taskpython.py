import numpy as np
import csv


with open("C:\\Users\\HP\\mca ai ml\\freshflow\\datasets\\freshflow_sales.csv", "r", newline="") as file:

    reader = csv.reader(file)


    headers = next(reader)


    rows = list(reader)


data = np.array(rows, dtype=float)

print("dataset loaded")


print("Shape:", data.shape)
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

print("Dimensions:", data.ndim)


print("Dimensions:", data.ndim)

print("Data Type:", data.dtype)

print(data[:5])
