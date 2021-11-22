#!/usr/bin/env python3

import json

data_json = {}

with open('data/json_00.json', 'r') as file:
    data_json = json.load(file)

print(data_json)

print(data_json[0])
print(data_json[1])
print(data_json[2])
print(data_json[3])
print(data_json[4])
print(data_json[5])
print(data_json[6])

print(data_json[5][0])
print(data_json[5][1])
print(data_json[5][2])
print(data_json[5][3])

print(data_json[6])
print(data_json[6]["A"])
print(data_json[6]["B"])
print(data_json[6]["C"])
print(data_json[6]["D"])
