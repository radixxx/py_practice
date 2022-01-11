# def sum_of_two_numbers(a=0, b=0):
#     '''
#
#     :param a:
#     :param b:
#     :return: sum of elements
#     '''
#     return a + b
#
#
# sum = sum_of_two_numbers()
# sum_2 = sum_of_two_numbers(5, 6)
#
#
# # print(sum, sum_2)
# # help(sum_of_two_numbers)
#
#
# def is_hello_in_text(text):
#     '''
#
#     :param text:
#     :return:
#     '''
#
#     if 'hello' in text.lower():
#         return True
#     else:
#         return False
#
#
# print(is_hello_in_text('Hello everyone'))
#
#
# def is_hello_in_text_2(text):
#     return 'hello' in text.lower()
#
#
# print(is_hello_in_text_2('Hello everyone'))
#
#
# def is_string_in_text(string, text):
#     return string in text
#
#
# print(is_string_in_text('hey', ' adsf'))


def product(*args):
    product = 1
    for number in args:
        product = product * number
    return product


print(product(5, 6, 7, 8, 9, 10))

#
# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
# #
# print(percent_of_product_with_args(5, 20, 3, 5, 10, 35))


# ###### task
# def is_cat_here(*args):
#     for string in args:
#         if 'cat' in string.lower():
#             return True
#     return False
#
#
# print(is_cat_here('Cat', 'dog ', 'bird'))
#
#
# def is_item_here(item, *args):
#     for string in args:
#         if item.lower() in string.lower():
#             return True
#     return False
#
#
# print(is_item_here('Cat', 'Cat ', 'bird'))
#
#
def your_favorite_colour(my_color, **kwargs):
    for key, value in kwargs.items():
        if 'colour' in key.lower():
            return "My favorite colour is " + my_color + ', but ' + value + ' is also pretty good!'
        else:
            return "My favorite colour is " + my_color + ', what is your favorite colour?'


print(your_favorite_colour('yellow', colour='red', name='Name', price='50'))
print(your_favorite_colour('green', number='green', name='Name'))