from file_handler.file_handler import FileHandler
import csv


class TSVFileHandler(FileHandler):
    def __init__(self, folder_path, file_name):
        super().__init__(folder_path, file_name)

    def read_file_data(self):
        with open(self.file_path) as file_ref:
            rows = csv.reader(file_ref, delimiter="\t", quotechar='"')
            self.file_data = list(rows)

    def format_file_data(self):
        data = list(filter(None, self.file_data))
        header = data.pop(0)
        formatted_rows = []
        for row in data:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[header[idx]] = value
            formatted_rows.append(row_dict)
        return formatted_rows
