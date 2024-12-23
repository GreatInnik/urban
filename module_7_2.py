from pprint import pprint

def custom_write(file_name, *strings):
    strings_positions = {}
    line_number = 1

    with open(file_name, 'w', encoding='utf-8') as file:
        for line in strings:
            byte_position = file.tell()
            file.write(line + '\n')
            strings_positions[(line_number, byte_position)] = line
            line_number += 1

    return strings_positions

positions = custom_write("info.txt", "Hello everyone", "How are you?", "Хорошая сегодня погода...")
pprint(positions)


