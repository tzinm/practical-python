# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, separator=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        if select and has_headers == False:
            raise RuntimeError("select argument requires column headers")

        rows = csv.reader(f, delimiter=separator)
        
        #Read the header of the files
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        
        records = []
        
        for rowno, row in enumerate(rows, 1):
            if not row:     #Skipping rows with no data
                continue

            if select:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func,val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
