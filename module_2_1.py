num1 = int(input('Введите первое число'))
num2 = int(input('Введите второе число'))
num3 = int(input('Введите третье число'))
if num1 == num2 and num2 == num3:
    print('3')
elif num1 == num2:
    print('2')
elif num2 == num3:
    print('2')
elif num1 == num3:
    print('2')
else:
    print('0')