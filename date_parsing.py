import calendar
import datetime


def get_year_month(_input):
    splitted_input = _input.split('/')
    year, month = splitted_input[0], splitted_input[1]
    month_name = calendar.month_name[int(month)][:3]
    return '{0}_{1}'.format(year, month_name)


def get_date_month(_input):
    dt = datetime.datetime.strptime(_input, '%Y-%m-%d')
    day = dt.day
    month = calendar.month_name[dt.month]
    return '{0} {1}'.format(month, day)
