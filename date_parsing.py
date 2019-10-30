import calendar


def get_year_month(_input):
    splitted_input = _input.split('/')
    year, month = splitted_input[0], splitted_input[1]
    month_name = calendar.month_name[int(month)][:3]
    return '{0}_{1}'.format(year, month_name)


def get_date_month(_input):
    splitted_input = _input.split('-')
    month, day = splitted_input[1], splitted_input[2]
    month = calendar.month_name[int(month)]
    return '{0} {1}'.format(month, day)
