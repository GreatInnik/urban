def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        if not isinstance(i, int):
            incorrect_data += 1
        else:
            result += i

    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):
        print("В numbers записан некорректный тип данных")
        return 0

    total_sum, incorrect_data = personal_sum(numbers)

    if len(numbers) - incorrect_data == 0:
        return 0

    return total_sum / (len(numbers) - incorrect_data)


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректный ввод
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать