from file_handler.file_handler import FileHandler


class TextFileHandler(FileHandler):
    def __init__(self, folder_path, file_name):
        super().__init__(folder_path, file_name)

    def read_file_data(self):
        with open(self.file_path, 'r') as file_ref:
            self.file_data = file_ref.read()

    def format_file_data(self):
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
