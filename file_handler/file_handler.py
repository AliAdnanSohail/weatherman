class FileHandler:
    def __init__(self, folder_path, file_name):
        self.folder_path = folder_path
        self.file_name = file_name
        self.file_path = folder_path + file_name
        self.file_data = []
        self.formatted_data = []
