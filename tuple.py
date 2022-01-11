
tuple_1 = (1, 2, 3, 4)
tuple_0 = 1, 2, 3, 4
tuple_2 = ('2', 'char')
tuple_3 = ('2', 'char', 5, 2.2)
new_tuple = (tuple_3[0], tuple_1[2], tuple_3[-1])

print(tuple_0)
print(tuple_2)
print(tuple_3)
print(type(tuple_0))
print(tuple_2)
print(new_tuple)
#
x = y = z = 12
print(x, y, z)
x, y, z, = 12, 13, 14
print(x, y, z)
person_tuple = ('John', 'Doe', 1988, 15.3)
first_name, last_name, year_of_birth, balance = person_tuple
print(first_name, last_name, year_of_birth, balance)
print(type(first_name), type(last_name), type(year_of_birth), type(balance))
t1 = (1, {1, 2, 3}, 5, 1, 7, 9)
print("printe t1", t1.index(9))
print("printe t1", t1.count(1))
# #
string_tuple = ('hola', 'hi',  'hi', 'hello')
print("hi is met", string_tuple.count('hi'), 'times')
print("index of 5 is", t1.index(5))
print("index of hi is", string_tuple.index('hi'))
#
computer_tuple = ('my_motherboard', 'CPU i9', 'RAM 16Gb', 'HDD 2 TB', 'SSD 512 GB', 'my_mouse', 'my_keyboard')
mother_board, cpu_model, ram, hdd_volume, ssd_volume, mouse, keyboard = computer_tuple
print(mother_board, cpu_model, ram, hdd_volume, ssd_volume, mouse, keyboard)
#

a = 5
b = 7
print('a', a, "b", b)
a, b = b, a
print("after", 'a', a, "b", b)
#
ultimate_tuple = tuple("ultimate tuple")
print(ultimate_tuple)