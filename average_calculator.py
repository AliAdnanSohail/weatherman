import file_handler
import date_parser


def display_average(path, date):
    date = date_parser.format_date(date, '%y_%M')

    zip_dir_name = 'weatherfiles'
    path = '{path}/{zip_dir_name}/'.format(path=path, zip_dir_name=zip_dir_name)
    files = file_handler.filter_files(path, date)
    if not files:
        print('No data found for {date}'.format(date=date))
        return

    formatted_data = file_handler.format_file_data(path, files[0])

    avg_max_temp = calculate_average(formatted_data, 'Max TemperatureC')
    avg_min_temp = calculate_average(formatted_data, 'Min TemperatureC')
    avg_mean_humidity = calculate_average(formatted_data, 'Mean Humidity')

    print(format_output('Max TemperatureC', avg_max_temp))
    print(format_output('Min TemperatureC', avg_min_temp))
    print(format_output('Mean Humidity', avg_mean_humidity))


def calculate_average(formatted_data, key):
    values = [int(d[key]) for d in formatted_data if d[key]]
    average = sum(values) / len(values)
    return round(average, 2)


def format_output(key, value):
    if key == 'Max TemperatureC':
        output_string = 'Highest Average: {value}C'.format(value=value)
    elif key == 'Min TemperatureC':
        output_string = "Lowest Average: {value}C".format(value=value)
    elif key == 'Mean Humidity':
        output_string = "Average Mean Humidity: {value}%".format(value=value)
    else:
        output_string = 'Invalid key'
    return output_string
