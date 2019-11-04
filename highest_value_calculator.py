import file_handler
import date_parser


def display_highest(path, year):
    zip_dir_name = 'weatherfiles'
    path = '{path}/{zip_dir_name}/'.format(path=path, zip_dir_name=zip_dir_name)
    files = file_handler.filter_files(path, year)
    if not files:
        print('No data found for {year}'.format(year=year))
        return

    highest_temp_row = None
    lowest_temp_row = None
    highest_humidity_row = None

    for file in files:
        formatted_data = file_handler.format_file_data(path, file)

        highest_temp_in_file = max(formatted_data, key=lambda d: int(d['Max TemperatureC']))
        lowest_temp_in_file = min(formatted_data, key=lambda d: int(d['Min TemperatureC']))
        highest_humidity_in_file = max(formatted_data, key=lambda d: int(d['Max Humidity']))

        highest_temp_row = get_max_or_min(highest_temp_row, highest_temp_in_file, 'Max TemperatureC', 'max')
        lowest_temp_row = get_max_or_min(lowest_temp_row, lowest_temp_in_file, 'Min TemperatureC', 'min')
        highest_humidity_row = get_max_or_min(highest_humidity_row, highest_humidity_in_file, 'Max Humidity', 'max')

    print(format_output(highest_temp_row, 'Max TemperatureC'))
    print(format_output(lowest_temp_row, 'Min TemperatureC'))
    print(format_output(highest_humidity_row, 'Max Humidity'))


def format_output(row, key):
    date = row.get('PKT') or row.get('PKST')
    date = date_parser.format_date(date, '%M %d')
    if key == 'Max TemperatureC':
        output_string = 'Highest: {temp}C on {date}'.format(temp=row[key], date=date)
    elif key == 'Min TemperatureC':
        output_string = 'Lowest: {temp}C on {date}'.format(temp=row[key], date=date)
    elif key == 'Max Humidity':
        output_string = 'Humidity: {humidity}% on {date}'.format(humidity=row[key], date=date)
    return output_string


def get_max_or_min(row, new_row, key, operator):
    if row is None:
        return new_row
    else:
        if operator == 'max':
            return max([row, new_row], key=lambda r: int(r[key]))
        elif operator == 'min':
            return min([row, new_row], key=lambda r: int(r[key]))
