from colorama import Fore, Style

import file_handler
import date_parser


def display_bar_chart(path, date):
    date = date_parser.format_date(date, '%y_%M')

    zip_dir_name = 'weatherfiles'
    path = '{path}/{zip_dir_name}/'.format(path=path, zip_dir_name=zip_dir_name)
    files = file_handler.filter_files(path, date)
    if not files:
        print('No data found for {date}'.format(date=date))
        return

    formatted_data = file_handler.format_file_data(path, files[0])
    display_chart(formatted_data)


def display_chart(formatted_data):
    for d in formatted_data:
        date = d.get('PKT') or d.get('PKST')
        __, __, day = date.split('-')
        if d['Max TemperatureC'] and d['Min TemperatureC']:
            display_bar_line(day, int(d['Max TemperatureC']), int(d['Min TemperatureC']))


def display_bar_line(date, max_val, min_val):
    print(Style.RESET_ALL)

    bar_line = '{heat_color}{heatline}{cold_color}{coldline}'.format(heat_color=Fore.RED,
                                                                     heatline='+'*max_val,
                                                                     cold_color=Fore.BLUE,
                                                                     coldline='+'*abs(min_val))

    unit = '{default_color}{max_val}C - {min_val}C'.format(default_color=Fore.WHITE,
                                                           max_val=max_val,
                                                           min_val=min_val)
    print(date, bar_line, unit)
