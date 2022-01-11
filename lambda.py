from functools import reduce

double_lambda = lambda x: x * 2
print(double_lambda(3))

items = [1, 2, 3, 4, 7, 7, 11]

print(list(filter(lambda x: (x % 2 != 0), items)))

print(list(filter(lambda x: (x >= 7), items)))

numbers = [5, 15, 9, 8, 9, 11]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)
max_value = reduce(lambda x, y: x if (x > y) else y, numbers)
print(max_value)

squared_list_lambda = list(map(lambda x: (x * x), items))
print("The squared numbers are", squared_list_lambda)

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5]

new_list = list(map(lambda x, y: x + y, list_1, list_2))
print(new_list)