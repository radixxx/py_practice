x = 1
y = 2

print(x > 1)
print(y > 1)

print('and', x > 1 and y > 1)
print('or', x > 1 or y > 1)
print('not', not x > 1)

x = 3

if x > 3:
    print('x>3')
elif x < 3:
    print('x<3')
else:
    print('x = 3')

# add more examples with if construtions

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# student tasks print only odd numbers from number_list
# calculate sum of elements

for number in number_list:
    print('Hi', number)
    print('Hello' + str(number * 2))

greeting = "Hello Python"

for letter in greeting:
    if letter != 'o':
        print(letter)

tuple_list = [('a', 'b', 1), ('c', 'd', 5), ('e', 'f', 6)]

for item in tuple_list:
    print(item)
for letter_1, letter_2, number in tuple_list:
    print(letter_1, letter_2, number)

my_dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for item in my_dictionary:
    print(item)

for item in my_dictionary.items():  # key values in tuple
    print(item)

for item in my_dictionary.keys():
    print(item)

for item in my_dictionary.values():
    print(item)

for key, values in my_dictionary.items():
    print(key)
    print(values)

for x in range(5):
    print(x + 1)
else:
    print('x is out of range')

for _ in range(5):  # iterator is not used
    print('Hello')

iterator = 1

while iterator <= 5:
    print(iterator)
    iterator += 1

x = 2
while x < 10:
    print('x less then 1')
    x += 1
else:
    print('x is equal 10')

while_list = [1, 2, 3]

for item in while_list:
    pass
# add example with break and continue

print('Go ahead')