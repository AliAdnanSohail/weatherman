import calendar
import datetime


class DateParser:
    def __init__(self, date, pattern):
        self.date = datetime.datetime.strptime(date, pattern)

    def format_date(self, pattern):
        if pattern == '%M %d':
            month_name = calendar.month_name[self.date.month]
            return '{month_name} {day}'.format(month_name=month_name, day=self.date.day)
        elif pattern == '%y_%M':
            month_name = calendar.month_name[self.date.month][:3]
            return '{year}_{month_name}'.format(year=self.date.year, month_name=month_name)
