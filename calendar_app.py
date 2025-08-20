import calendar
import datetime

def display_current_month_calendar():
    now = datetime.datetime.now()
    print(calendar.month(now.year, now.month))
