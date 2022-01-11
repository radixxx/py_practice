rainbow_colours = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colours)
print(type(rainbow_colours))
empty_set = {}
print(type(empty_set))

empty_set_set = set()
print(type(empty_set_set))
#
number_list = [1, 43, 52, 43]
text_tuple = ('asd', 'qwe', 'zxc', 'asd')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

print(set_from_list)
print(set_from_tuple)
#
# set_from_list.add(555)
# set_from_tuple.add('string')
# #
# # # returns value
# x = set_from_list.pop()
# print( 'The ', x, 'value was removed from set')
# #
# # error if key doesn't exist, doesn't return value
# set_from_list.remove(43)
# #
# # # do nothing if key doesn't exist, , doesn't return value
# set_from_list.discard(43)
# #
# # #  remove all elements from set
# # set_from_list.clear()
# #
# print(set_from_list)
# print(set_from_tuple)
#
my_text = 'Hello world!'
set_from_string = set(my_text)
print(set_from_string)