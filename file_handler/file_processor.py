from file_handler.text_file_handler import TextFileHandler
from file_handler.excel_file_handler import ExcelFileHandler
from file_handler.tsv_file_handler import TSVFileHandler


class FileProcessor:
    def __init__(self, folder_path, file_name):
        self.folder_path = folder_path
        self.file_name = file_name

    def format_file_data(self):
        if self.file_name.endswith('.txt'):
            text_file = TextFileHandler(self.folder_path, self.file_name)
            text_file.read_file_data()
            return text_file.format_file_data()
        elif self.file_name.endswith('.xlsx'):
            excel_file = ExcelFileHandler(self.folder_path, self.file_name)
            excel_file.read_file_data()
            return excel_file.format_file_data()
        elif self.file_name.endswith('.tsv'):
            tsv_file = TSVFileHandler(self.folder_path, self.file_name)
            tsv_file.read_file_data()
            return tsv_file.format_file_data()
        else:
            raise Exception('Invalid file extension')
