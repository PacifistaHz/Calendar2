import calendar

def print_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(cal.formatmonth(year, month))

year = int(input("Enter year: "))
month = int(input("Enter month (1 between 12): "))

print_calendar(year, month)
