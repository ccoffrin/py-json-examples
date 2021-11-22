#!/usr/bin/env python3

import csv

rows = []

with open('data/table_01.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)

print(rows)
print(rows[0])
print(rows[1])
print(rows[1][2])



header = rows[0]

data_rows = rows[1:]

data_rows_float = [[float(item) for item in row] for row in data_rows]

print(data_rows_float)

