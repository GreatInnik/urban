def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c = [1,2,3])

values_list = [False, 'List', 4]
values_dict = {'a': 'Mercy', 'b': 6, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [404, 'Huge']

print_params(*values_list_2, 42)