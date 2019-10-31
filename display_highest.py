import file_handling
import date_parsing


def display_highest_values(path, year):
    files = file_handling.get_relevant_files(path, year)

    highest_temp_row = None
    highest_low_temp_row = None
    highest_humidity_row = None

    for file in files:
        raw_data = file_handling.read_file(path, file)
        formatted_data = file_handling.format_file_data(raw_data)

        highest_temp_in_file = get_max_rows(formatted_data,
                                            'Max TemperatureC',
                                            True)

        highest_low_temp_in_file = get_max_rows(formatted_data,
                                                'Min TemperatureC')

        highest_humidity_in_file = get_max_rows(formatted_data,
                                                'Max Humidity',
                                                True)

        highest_temp_row = get_max(highest_temp_row,
                                   highest_temp_in_file,
                                   'Max TemperatureC')

        highest_low_temp_row = get_min(highest_low_temp_row,
                                       highest_low_temp_in_file,
                                       'Min TemperatureC')

        highest_humidity_row = get_max(highest_humidity_row,
                                       highest_humidity_in_file,
                                       'Max Humidity')

    format_output(highest_temp_row, 'Max TemperatureC')
    format_output(highest_low_temp_row, 'Min TemperatureC')
    format_output(highest_humidity_row, 'Max Humidity')


def format_output(row, key):
    if 'PKT' in row:
        date = row['PKT']
    else:
        date = row['PKST']

    date = date_parsing.get_date_month(date)
    if key == 'Max TemperatureC':
        print('Highest:', row[key] + 'C on', date)
    if key == 'Min TemperatureC':
        print('Lowest:', row[key] + 'C on', date)
    if key == 'Max Humidity':
        print('Humidity:', row[key] + '% on', date)


def get_max_rows(formatted_rows, key, reverse=False):
    formatted_rows = [i for i in formatted_rows if i[key] != '']
    sorted_data = sorted(formatted_rows,
                         key=lambda i: int(i[key]),
                         reverse=reverse)
    return sorted_data[0]


def get_max(max_row, new_row, key):
    max_row_is_none = max_row is None

    if max_row_is_none or int(new_row[key]) > int(max_row[key]):
        return new_row
    else:
        return max_row


def get_min(min_row, new_row, key):
    min_row_is_none = min_row is None

    if min_row_is_none or int(new_row[key]) < int(min_row[key]):
        return new_row
    else:
        return min_row
