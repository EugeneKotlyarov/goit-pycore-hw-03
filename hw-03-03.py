# function accepts phone number as string in any format
# and returns normalized number as string in format:
# +380991235343 (as example)

import re


def normalize_phone(phone_number: str) -> str:

    # remove any symbols but numbers
    pattern = re.compile(r"\D")
    total_digits = re.sub(pattern, "", phone_number)

    # get right 9 digits: 2 for operator code, 7 for number and ignore others
    if len(total_digits) < 9:
        # return error if number is less than 9 digits
        return f"entered number '{phone_number}' is not valid, error: too short"
    else:
        crop_start = len(total_digits) - 9
        right_9_digits = total_digits[crop_start:]

    # check corrects of the first 2 (operator) digits
    pattern_operator_validation = re.compile(
        f"^(50|66|95|99|75|67|68|96|97|98|63|73|93|91|92|94)"
    )
    if re.search(pattern_operator_validation, right_9_digits):
        # valid UA operator number
        return str(f"+380{right_9_digits}")
    else:
        # invalid code
        return str(
            f"entered number '{right_9_digits}; is not valid, error: '{right_9_digits[:2]}' is not ukrainian mobile operator code"
        )


# test
# invalid
print(normalize_phone(" +380/90/21-55-888 "))
# invalid
print(normalize_phone("9/21-55-888 "))
# valid
print(normalize_phone(" +380/97/21-55-888 , "))
