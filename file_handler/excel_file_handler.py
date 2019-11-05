from file_handler.file_handler import FileHandler
from pandas import read_excel


class ExcelFileHandler(FileHandler):
    def __init__(self, folder_path, file_name):
        super().__init__(folder_path, file_name)

    def read_file_data(self):
        self.file_data = read_excel(self.file_path)

    def format_file_data(self):
        formatted_rows = self.file_data.to_dict('records')
        return formatted_rows
