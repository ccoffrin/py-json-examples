# py-json-examples

Examples of working with JSON data in Python

## Outline

- Reading CSV data in python (see `csv-read.py`)
  - types of data (string / float / int / boolean)
  - missing data
  - column names
  - better solution? if data is truely tabular use "dataframes" (see pandas)
  - but what if the data is not tabular?

- What is JSON? (see `data/json_00.json`)
  - data types, string / float / int / boolean, null
  - resursive design
  - very easy to parse

- Reading JSON data in pyhton (see `json-read.py`)
  - python data structure built automatically
  - data types encoded automatically

- Data encoding ideas (see `json-encoding.py`)
  - array of arrays (row-first, csv like) `json_table_01.json`
  - dict of arrays (column-first, dataframe like) `json_table_02.json`
  - array of dicts (map, object like) `json_table_03.json`

- CSV to JSON
  - pick a JSON encoding
  - perform data structure manipulations in python into a dict
  - write JSON
  - basic solution `csv-to-json-01.py`
  - more advanced solution `csv-to-json-02.py`
