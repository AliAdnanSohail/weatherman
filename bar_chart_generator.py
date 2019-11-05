from weatherman_helper import display_bar_line
from date_parser import DateParser
from file_record import FileRecord


class BarChartGenerator(FileRecord):
    def __init__(self, zip_file_ref, duration):
        super().__init__(zip_file_ref, duration)

    def display_bar_chart(self):
        date = DateParser(self.duration, '%Y/%m').format_date(pattern='%y_%M')

        files_name = self.get_files_name(date)
        for file_name in files_name:
            self.display_chart_for_file(file_name)

    def display_chart_for_file(self, file_name):
        formatted_data = self.get_formatted_data(file_name)

        for d in formatted_data:
            date = d.get('PKT') or d.get('PKST')
            day = DateParser(date, '%Y-%m-%d').date.day
            if d['Max TemperatureC'] and d['Min TemperatureC']:
                display_bar_line(day, int(d['Max TemperatureC']), int(d['Min TemperatureC']))
