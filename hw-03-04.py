# function get_upcoming_birthdays accepts list of dictionaries with employers birthdays
# and return list of dictionaries with dates when to greetings them
# weekends is moving to the next monday

from datetime import datetime as dt
from datetime import timedelta as tdelta


def get_upcoming_birthdays(users: list) -> list:

    # result structute for return
    notifications = []

    # get today values: date, year, number of the current day in year and total days is year

    # use next two lines to check fuctionality
    # today_date = dt.(2024, 12, 30).date()
    today_date = dt.today().date()

    today_year = today_date.year
    today_number_in_year = today_date.timetuple().tm_yday
    ny_number_in_year = dt(today_year, 12, 31).timetuple().tm_yday

    for user in users:

        # for current user found
        # his original birth date
        # his birthday this year
        # day number of birthday in year
        user_bd_original = dt.strptime(user["birthday"], "%Y.%m.%d").date()
        user_bd_this_year = dt(
            year=today_year, month=user_bd_original.month, day=user_bd_original.day
        ).date()
        user_bd_this_year_number = user_bd_this_year.timetuple().tm_yday

        # simple situation if birthday within a week from now
        if 0 <= user_bd_this_year_number - today_number_in_year <= 7:

            congratulation_date = user_bd_this_year

            # weekend days check and move date to monday if true
            if congratulation_date.isoweekday() >= 6:
                congratulation_date += tdelta(8 - congratulation_date.isoweekday())

            # create and append dict to result list
            user_to_congratulate = {}
            user_to_congratulate["name"] = user["name"]
            user_to_congratulate["congratulation_date"] = congratulation_date.strftime(
                "%Y.%m.%d"
            )
            notifications.append(user_to_congratulate)

        # situation at the end of year and birthday on january begin
        elif ny_number_in_year - today_number_in_year + user_bd_this_year_number <= 7:

            # congratulation_date must be set to next year
            congratulation_date = dt(
                year=today_year + 1,
                month=user_bd_original.month,
                day=user_bd_original.day,
            )

            # weekend days check and move date to monday if true
            if congratulation_date.isoweekday() >= 6:
                congratulation_date += tdelta(8 - congratulation_date.isoweekday())

            # create and append dict to result list
            user_to_congratulate = {}
            user_to_congratulate["name"] = user["name"]
            user_to_congratulate["congratulation_date"] = congratulation_date.strftime(
                "%Y.%m.%d"
            )
            notifications.append(user_to_congratulate)

    return notifications


# test
users = [
    {"name": "John Doe", "birthday": "1985.10.11"},  # true
    {"name": "Jane Smith", "birthday": "1990.10.12"},  # true
    {"name": "Jahne Kohen", "birthday": "1996.01.04"},  # false
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
