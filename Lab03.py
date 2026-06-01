# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program displays what any month of any year would look like on a calendar 
#       (within the bounds of the current calendar system)
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was sorting through which parts of my previous code (from 
#       last semester) would be helpful. I initially brought over the entire function, 
#       only to realize that most of it wasn't needed. In any case, being able to reuse 
#       the code made this a lot easier.
# 5. How long did it take for you to complete the assignment?
#      1 hour and 15 minutes



def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and year > 1752

def compute_offset(year, month):
    
    assert all(isinstance(i, int) for i in (year, month)), "All inputs must be integers"
    assert year >= 1753, "Year too early"
    assert month > 0, "Month cannot be less than 1"
    assert month < 13, "Month cannot be greater than 12"
    
    num_days = 0
    for year_count in range(1753, year):
        num_days += days_year(year_count)
    for month_count in range(1, month):
        num_days += days_month(month_count, year)
    return (num_days + 1) % 7

def days_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365
def days_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else: # February
        if not is_leap_year(year):
            return 28
        else:
            return 29



def calculate_calendar_month(year, month):
    offset = compute_offset(year, month)
    month_length = days_month(month, year)
    # Output
    print()
    print(f"{month}/{year}")
    display_table(offset, month_length)


def main():
    # year, month
    calculate_calendar_month(1753, 1)
    blank = input()
    calculate_calendar_month(1753, 2)
    blank = input()
    calculate_calendar_month(1754, 1)
    blank = input()
    calculate_calendar_month(1756, 2)
    blank = input()
    calculate_calendar_month(1800, 2)
    blank = input()
    calculate_calendar_month(2000, 2)
    blank = input()
    calculate_calendar_month(2019, 11)
    # Errors
    calculate_calendar_month(1753, 13)
    # calculate_calendar_month('error', 'error')
    # calculate_calendar_month(-1, 0)



main()
