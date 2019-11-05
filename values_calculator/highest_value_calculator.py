from helpers.weatherman_helper import format_highest_values_output
from values_calculator.file_record import FileRecord


class HighestValueCalculator(FileRecord):
    def __init__(self, zip_file_ref, duration):
        super().__init__(zip_file_ref, duration)

    def display_highest(self):
        highest_temp_row = None
        lowest_temp_row = None
        highest_humidity_row = None

        files_name = self.get_files_name(self.duration)
        for file_name in files_name:
            formatted_data = self.get_formatted_data(file_name)

            highest_temp_in_file = max(formatted_data, key=lambda r: int(r.get('Max TemperatureC')))
            lowest_temp_in_file = min(formatted_data, key=lambda r: int(r.get('Min TemperatureC')))
            highest_humidity_in_file = max(formatted_data, key=lambda r: int(r.get('Max Humidity')))

            highest_temp_row = max([(highest_temp_row or highest_temp_in_file), highest_temp_in_file],
                                   key=lambda r: int(r.get('Max TemperatureC')))
            lowest_temp_row = min([(lowest_temp_row or lowest_temp_in_file), lowest_temp_in_file],
                                  key=lambda r: int(r.get('Min TemperatureC')))
            highest_humidity_row = max([(highest_humidity_row or highest_humidity_in_file), highest_humidity_in_file],
                                       key=lambda r: int(r.get('Max Humidity')))

        print(format_highest_values_output(highest_temp_row, 'Max TemperatureC'))
        print(format_highest_values_output(lowest_temp_row, 'Min TemperatureC'))
        print(format_highest_values_output(highest_humidity_row, 'Max Humidity'))
