# function returns int value as days between input text date and today
# > 0 if date from the past
# and
# < 0 if date from the future

from datetime import datetime as dt


# please use "YYYY-MM-DD" as input
def get_days_from_today(date_from_str: str) -> int:

    # input value check
    try:
        date_from_dt = dt.strptime(date_from_str, "%Y-%m-%d")
    except ValueError as error:
        print(f'Error in input! Usage: get_days_from_today("YYYY-MM-DD")')

    return int((dt.now() - date_from_dt).days)


# test
print(get_days_from_today("2023-10-12"))
print(get_days_from_today("2024-12-21"))
