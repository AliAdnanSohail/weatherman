import csv
from pandas import read_excel


class FileProcessor:
    def __init__(self, folder_path, file_name):
        self.folder_path = folder_path
        self.file_name = file_name
        self.file_path = folder_path + file_name
        self.file_data = []
        self.formatted_data = []

    def format_file_data(self):
        if self.file_name.endswith('.txt'):
            self.read_text_file_data()
            return self.format_text_file_data()
        elif self.file_name.endswith('.xlsx'):
            self.read_excel_file_data()
            return self.format_excel_file_data()
        elif self.file_name.endswith('.tsv'):
            self.read_tsv_file_data()
            return self.format_tsv_file_data()
        else:
            raise Exception('Invalid file extension')

    def read_text_file_data(self):
        with open(self.file_path, 'r') as file_ref:
            self.file_data = file_ref.read()

    def read_excel_file_data(self):
        self.file_data = read_excel(self.file_path)

    def read_tsv_file_data(self):
        with open(self.file_path) as file_ref:
            rows = csv.reader(file_ref, delimiter="\t", quotechar='"')
            self.file_data = list(rows)

    def format_text_file_data(self):
        rows = self.file_data.split('\n')
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

    def format_excel_file_data(self):
        formatted_rows = self.file_data.to_dict('records')
        return formatted_rows

    def format_tsv_file_data(self):
        data = list(filter(None, self.file_data))
        header = data.pop(0)
        formatted_rows = []
        for row in data:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[header[idx]] = value
            formatted_rows.append(row_dict)
        return formatted_rows
