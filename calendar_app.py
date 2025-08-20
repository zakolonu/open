import calendar
import datetime

def display_current_month_calendar():
    now = datetime.datetime.now()
    print(calendar.month(now.year, now.month))

def display_specific_month_calendar(year, month):
    print(calendar.month(year, month))

