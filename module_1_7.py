grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = tuple(students)
students = sorted(students)
print(students)

a = grades.pop(0)
new_a = sum(a)/5
b = grades.pop(-4)
new_b = sum(b)/4
c = grades.pop(-3)
new_c = sum(c)/5
d = grades.pop(-2)
new_d = sum(d)/3
e = grades.pop(-1)
new_e = sum(e)/5

n1 = students[0]
n2 = students[1]
n3 = students[2]
n4 = students[3]
n5 = students[4]

my_set = {str(n1): new_a, str(n2): new_b, str(n3): new_c, str(n4): new_d, str(n5): new_e}
print(my_set)