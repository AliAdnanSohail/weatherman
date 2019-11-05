from file_processor import FileProcessor


class FileRecord:
    def __init__(self, zip_file_ref, duration):
        self.zip_file_ref = zip_file_ref
        self.duration = duration

    def get_files_name(self, date):
        files_name = self.zip_file_ref.filter_files(date)
        if not files_name:
            print('No data found for {duration}'.format(duration=self.duration))
            return
        return files_name

    def get_formatted_data(self, file_name):
        file_processor = FileProcessor(self.zip_file_ref.directory_path, file_name)
        return file_processor.format_file_data()
