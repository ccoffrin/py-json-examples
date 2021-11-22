#!/usr/bin/env python3

import csv, json

BUS_ID_COL = 0
NAME_COL = 1
VM_COL = 2
VA_COL = 3
BASE_KV_COL = 4

rows = []

with open('data/table_01.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        rows.append(row)

data_rows = rows[1:]

json_data = []

for row in data_rows:
    bus_data = {
        "bus_id": int(row[BUS_ID_COL]),
        "name": row[NAME_COL].strip(),
        "vm": float(row[VM_COL]),
        "va": float(row[VA_COL]),
        "base_kv": float(row[BASE_KV_COL])
    }
    json_data.append(bus_data)

print(json_data)

with open('data/table_02-tmp.json', 'w') as file:
    json.dump(json_data, file, indent=2, sort_keys=True)

