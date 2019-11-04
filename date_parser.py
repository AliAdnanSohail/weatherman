import calendar


def format_date(date, pattern):
    if pattern == '%M %d':
        __, month, day = date.split('-')
        month_name = calendar.month_name[int(month)]
        return '{month_name} {day}'.format(month_name=month_name, day=day)
    elif pattern == '%y_%M':
        year, month = date.split('/')
        month_name = calendar.month_name[int(month)][:3]
        return '{year}_{month_name}'.format(year=year, month_name=month_name)
