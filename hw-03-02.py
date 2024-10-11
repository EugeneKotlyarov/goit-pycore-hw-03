# function returns sorted quantity unique numbers as list
# in range between min and max values
# or
# empty list if error in parameters input
# where min >= 1 and max <= 1000

import random as rnd


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    # parameters checking with return of empty list if value or logical error
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min):
        print("we are here")
        return list()

    # main code
    # initialize set with minimum 1 element
    working_set = {rnd.randint(min, max)}

    # increment set length till the quantity value
    while len(working_set) < quantity:
        working_set.add(rnd.randint(min, max))

    # returnig sorted set converted to list type
    return list(sorted(working_set))


# test
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")
