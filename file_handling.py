import os
import zipfile


def extract_file(path='default'):
    with zipfile.ZipFile('weatherfiles.zip', 'r') as zip_ref:
        zip_ref.extractall(path)
        zip_ref.close()
    return path


def get_relevant_files(path, to_find):
    path = path + '/weatherfiles'
    all_files = os.listdir(path)
    return [f for f in all_files if f.__contains__(to_find)]


def read_file(path, file_name):
    file_path = path + '/weatherfiles/' + file_name
    with open(file_path, 'r') as file:
        read_data = file.read()
        file.close()

    return read_data


def format_file_data(data):
    rows = data.split('\n')
    header = rows.pop(0).split(',')
    formatted_rows = []
    for row in rows:
        row_dict = {}
        row_data = row.split(',')
        for i in range(len(row_data)):
            row_dict[header[i].strip()] = row_data[i]
        formatted_rows.append(row_dict)
    formatted_rows.pop(-1)
    return formatted_rows
