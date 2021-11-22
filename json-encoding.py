#!/usr/bin/env python3

import json

data_json = {}

with open('data/json_table_01.json', 'r') as file:
    data_json = json.load(file)

print(data_json)


with open('data/json_table_02.json', 'r') as file:
    data_json = json.load(file)

print(data_json)


with open('data/json_table_03.json', 'r') as file:
    data_json = json.load(file)

print(data_json)


with open('data/json_multitable.json', 'r') as file:
    data_json = json.load(file)

print(data_json)

