import calendar
import datetime

def display_current_month_calendar():
    now = datetime.datetime.now()
    print(calendar.month(now.year, now.month))

def display_specific_month_calendar(year, month):
    try:
        year = int(year)
        month = int(month)
        if not (1 <= month <= 12):
            print("Error: Month must be between 1 and 12.")
            return
        print(calendar.month(year, month))
    except ValueError:
        print("Error: Invalid year or month. Please enter numeric values.")



