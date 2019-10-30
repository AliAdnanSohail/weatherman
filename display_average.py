import file_handling
import date_parsing


def display_average_values(path, _input):
    date = date_parsing.get_year_month(_input)

    files = file_handling.get_relevant_files(path, date)
    data = file_handling.read_file(path, files[0])
    formatted_data = file_handling.format_file_data(data)

    avg_max_temp = calculate_average(formatted_data, 'Max TemperatureC')
    avg_min_temp = calculate_average(formatted_data, 'Min TemperatureC')
    avg_mean_humidity = calculate_average(formatted_data, 'Mean Humidity')

    format_output('Max TemperatureC', avg_max_temp)
    format_output('Min TemperatureC', avg_min_temp)
    format_output('Mean Humidity', avg_mean_humidity)


def calculate_average(formatted_data, key):
    values = [int(d[key]) for d in formatted_data if d[key] != '']
    average = sum(values)/len(values)
    return average


def format_output(key, value):
    if key == 'Max TemperatureC':
        print("Highest Average:", str(value) + 'C')

    if key == 'Min TemperatureC':
        print("Lowest Average:", str(value) + 'C')

    if key == 'Mean Humidity':
        print("Average Mean Humidity:", str(value) + '%')
