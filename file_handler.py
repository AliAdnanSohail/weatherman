import os
import zipfile
import fnmatch
import csv
import pandas


def extract_file(path, zip_name):
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(path)


def filter_files(path, pattern):
    all_files_name = os.listdir(path)
    filtered_name = fnmatch.filter(all_files_name, '*{pattern}*'.format(pattern=pattern))
    return filtered_name


def format_file_data(path, file_name):
    file_path = path + file_name

    if file_path.endswith('.txt'):
        raw_data = read_text_file_data(file_path)
        return format_text_file_data(raw_data)
    elif file_path.endswith('.xlsx'):
        raw_data = read_xlsx_file_data(file_path)
        return format_xlsx_file_data(raw_data)
    elif file_path.endswith('.tsv'):
        raw_data = read_tsv_file_data(file_path)
        return format_tsv_file_data(raw_data)
    else:
        raise Exception('Invalid file extension')


def read_text_file_data(file_path):
    with open(file_path, 'r') as file_ref:
        read_data = file_ref.read()
    return read_data


def format_text_file_data(data):
    rows = data.split('\n')
    rows = list(filter(None, rows))
    header = rows.pop(0).split(',')
    header = list(map(str.strip, header))
    formatted_rows = []
    for row in rows:
        row_dict = {}
        row_data = row.split(',')
        for idx, value in enumerate(row_data):
            row_dict[header[idx]] = value
        formatted_rows.append(row_dict)
    return formatted_rows


def read_tsv_file_data(file_path):
    with open(file_path) as file_ref:
        rows = csv.reader(file_ref, delimiter="\t", quotechar='"')
        rows = list(rows)
    return rows


def format_tsv_file_data(data):
    data = list(filter(None, data))
    header = data.pop(0)
    formatted_rows = []
    for row in data:
        row_dict = {}
        for idx, value in enumerate(row):
            row_dict[header[idx]] = value
        formatted_rows.append(row_dict)
    return formatted_rows


def read_xlsx_file_data(file_path):
    data = pandas.read_excel(file_path)
    return data


def format_xlsx_file_data(data):
    formatted_rows = data.to_dict('records')
    return formatted_rows
