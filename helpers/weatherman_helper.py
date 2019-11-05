from colorama import Fore, Style
from date_parser import DateParser


def display_bar_line(date, max_val, min_val):
    print(Style.RESET_ALL)

    bar_line = '{heat_color}{heat_line}{cold_color}{cold_line}'.format(heat_color=Fore.RED,
                                                                       heat_line='+' * max_val,
                                                                       cold_color=Fore.BLUE,
                                                                       cold_line='+' * abs(min_val))

    unit = '{default_color}{max_val}C - {min_val}C'.format(default_color=Fore.WHITE,
                                                           max_val=max_val,
                                                           min_val=min_val)
    print(date, bar_line, unit)


def format_average_values_output(key, value):
    if key == 'Max TemperatureC':
        output_string = 'Highest Average: {value}C'.format(value=value)
    elif key == 'Min TemperatureC':
        output_string = "Lowest Average: {value}C".format(value=value)
    elif key == 'Mean Humidity':
        output_string = "Average Mean Humidity: {value}%".format(value=value)
    else:
        output_string = 'Invalid key'
    return output_string


def format_highest_values_output(row, key):
    date = row.get('PKT') or row.get('PKST')
    date = DateParser(date, '%Y-%m-%d').format_date(pattern='%M %d')
    if key == 'Max TemperatureC':
        output_string = 'Highest: {temp}C on {date}'.format(temp=row[key], date=date)
    elif key == 'Min TemperatureC':
        output_string = 'Lowest: {temp}C on {date}'.format(temp=row[key], date=date)
    elif key == 'Max Humidity':
        output_string = 'Humidity: {humidity}% on {date}'.format(humidity=row[key], date=date)
    return output_string


def calculate_average(formatted_data, key):
    values = [int(d[key]) for d in formatted_data if d[key]]
    average = sum(values) / len(values)
    return round(average, 2)
