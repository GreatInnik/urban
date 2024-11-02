my_dict = {'Fedor': 2005, 'Alex': 1999}
print(my_dict)
print(my_dict.get("Fedor"))
print(my_dict.get("Anna"))
my_dict.update({'Richard': 1995, 'Michael': 2002})
a = my_dict.pop('Richard')
print(a)
print(my_dict)

my_set = {1, 2, 3, 1, 2, True, False, True, 'Robot', 'Human', 'Human'}
print(my_set)
print(my_set.add('Apple'))
print(my_set.add(6))
print(my_set.discard(False))
print(my_set)