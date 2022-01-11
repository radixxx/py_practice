number_list = [32, 21, 45.2]
print(type(number_list))
some_list = [12, 'hello', 0, 25]
print(some_list)
print(len(some_list))
print(some_list[1])
print(some_list[3])
another_list = some_list[:2]
print("another_list", another_list)
some_list[1] = 'hi'
print(some_list[1])
print("some_list", some_list)
new_list = some_list + another_list
print(new_list)
new_list.append("new_item")
print(new_list)
new_list.insert(0, 'start')
new_list.insert(5, 'insert_item')
print(new_list)

# new_list.pop(-1)  # delete by index
# deleted_item = new_list.pop(-1)

# new_list.pop(0)
new_list.remove(12)
new_list.remove(12)
# new_list.remove(12)
print(new_list)
#
#
# # delete by value, first appearence
#
# print(new_list)
# print(deleted_item)
#
unsorted_list = [55, 44, 12, 62, 32]
# sorted_list = unsorted_list.sort()
# # result -> None; Important: Do not use concat (+) if one of the values mb None
print("sorted_list err",  unsorted_list.sort())
sorted_list = unsorted_list
print(sorted_list)
print(len(sorted_list))
# # result - >sorted
print("unsorted_list after sorting", unsorted_list)
# # result ->sorted
# print("sorted_list good result", sorted_list)
reverse_list = sorted_list.reverse()
print("reverse none", reverse_list)
print("reverse good", sorted_list)
letter_list = ['a', 'b', 'c']
print("letter list", letter_list)
number_list.append('Append' + letter_list[2])
print(letter_list.append(number_list))
print(number_list)