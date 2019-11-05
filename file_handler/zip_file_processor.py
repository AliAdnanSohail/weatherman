import os
import zipfile
import fnmatch


class ZipFileProcessor:
    def __init__(self, path, zip_name, directory_name):
        self.path = path
        self.zip_name = zip_name
        self.directory_path = '{path}/{directory_name}/'.format(path=self.path, directory_name=directory_name)

    def extract_files(self):
        with zipfile.ZipFile(self.zip_name, 'r') as zip_ref:
            zip_ref.extractall(self.path)

    def filter_files(self, pattern):
        all_files_name = os.listdir(self.directory_path)
        filtered_name = fnmatch.filter(all_files_name, '*{pattern}*'.format(pattern=pattern))
        return filtered_name
