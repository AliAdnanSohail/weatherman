from colorama import Fore, Back, Style

import file_handling
import date_parsing


def display_bar_chart(path, _input):
    date = date_parsing.get_year_month(_input)
    files = file_handling.get_relevant_files(path, date)
    data = file_handling.read_file(path, files[0])
    formatted_data = file_handling.format_file_data(data)
    display_chart(formatted_data)


def display_chart(formatted_data):
    for d in formatted_data:
        if 'PKT' in d:
            date = d['PKT'].split('-')[2]
        else:
            date = d['PKST'].split('-')[2]

        # Uncomment below code for separate bar
        # chart for max and mix temperature

        # if d['Max TemperatureC'] != '':
        #     display(date, int(d['Max TemperatureC']), Fore.RED)

        # if d['Min TemperatureC'] != '':
        #     display(date, int(d['Min TemperatureC']), Fore.BLUE)

        if d['Max TemperatureC'] != '' and d['Min TemperatureC'] != '':
            display_in_one_line(date,
                                int(d['Max TemperatureC']),
                                int(d['Min TemperatureC']))


def display(date, value, color):
    print(Style.RESET_ALL)
    orig_value = value

    # For negative values
    if value < 0:
        value = -1*value

    bar_line = color + '+' * value
    unit = Fore.WHITE + str(orig_value) + 'C'
    print(date, bar_line, unit)


def display_in_one_line(date, max_val, min_val):
    print(Style.RESET_ALL)
    orig_min_value = min_val

    # For negative values
    if min_val < 0:
        min_val = -1 * min_val

    bar_line = Fore.RED + '+'*max_val + Fore.BLUE + '+'*min_val
    unit = Fore.WHITE + str(max_val) + 'C - ' + str(orig_min_value) + 'C'
    print(date, bar_line, unit)
