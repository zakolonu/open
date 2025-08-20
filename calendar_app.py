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


def main():
    while True:
        print("
        print("1. Display current month's calendar")
        print("2. Display specific month's calendar")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_current_month_calendar()
        elif choice == '2':
            year = input("Enter year: ")
            month = input("Enter month: ")
            display_specific_month_calendar(year, month)
        elif choice == '3':
            print("Exiting calendar application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




