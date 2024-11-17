def get_multiplied_digits(number):
    if number == 0:
        return number
    str_number = str(number)
    first = int(str_number[0])

    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(1002))