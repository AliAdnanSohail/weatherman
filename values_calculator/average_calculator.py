from date_parser import DateParser
from values_calculator.file_record import FileRecord
from helpers.weatherman_helper import calculate_average, format_average_values_output


class AverageCalculator(FileRecord):
    def __init__(self, zip_file_ref, duration):
        super().__init__(zip_file_ref, duration)

    def display_average(self):
        date = DateParser(self.duration, '%Y/%m').format_date(pattern='%y_%M')

        files_name = self.get_files_name(date)
        for file_name in files_name:
            self.display_average_for_file(file_name)

    def display_average_for_file(self, file_name):
        formatted_data = self.get_formatted_data(file_name)

        avg_max_temp = calculate_average(formatted_data, 'Max TemperatureC')
        avg_min_temp = calculate_average(formatted_data, 'Min TemperatureC')
        avg_mean_humidity = calculate_average(formatted_data, 'Mean Humidity')

        print(format_average_values_output('Max TemperatureC', avg_max_temp))
        print(format_average_values_output('Min TemperatureC', avg_min_temp))
        print(format_average_values_output('Mean Humidity', avg_mean_humidity))
