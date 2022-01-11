# car_prices = {'opel': 5000, 'toyota': 7000, ' bmw': 10000}
# print(car_prices)
# print(car_prices['toyota'])
# car_prices['mazda'] = 4000
# print(car_prices)
# car_prices['opel'] = 2000
# print("new prices", car_prices)
# del car_prices['toyota']
# print(car_prices)
# #delete all dictionary with var,
# # del car_prices
# # print(car_prices)
# #delete values from dictionary
# car_prices.clear()
# print(car_prices)

################################
person = {
    'first name': 'John',
    'last name': 'Doe',
    'age': 40,
    'hobbies': ['football', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Luna'}
}
print("Person age", person['age'])
print("Person hobbies", person['hobbies'])
hobbies = person['hobbies']
print("Most payed hobby is", hobbies[1])
print("Most preferable hobby is", person['hobbies'][0])
person['car'] = 'hyundai'
person['hobbies'][0]='volley'
print(person)
print(person.keys())
print(person.values())
print(person.items())