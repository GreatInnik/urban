def get_multiplied_digits(number):
    if number == 0:
        return 1  # Изменяем на 1, чтобы не влиять на произведение
    str_number = str(number)
    first = int(str_number[0])

    # Игнорируем нули в конце числа
    while str_number and str_number[-1] == '0':
        str_number = str_number[:-1]

    if not str_number:  # Если все цифры были нулями
        return 1

    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(100420))