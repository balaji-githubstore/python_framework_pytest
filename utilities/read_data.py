import csv
import pandas


def get_csv_data(file_name):
    rows = []
    data_file = open(file_name, "r")
    reader = csv.reader(data_file)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows


def get_sheet_data(file_name, sheet_name):
    rows=[]
    df = pandas.read_excel(file_name, sheet_name=sheet_name)
    for i in df.index:
        rows.append(df.loc[i].tolist())
    print(rows)
    return rows