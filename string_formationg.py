name = 'Jack'
age = 23
print('Jack is ' + str(age) + ' years old.')
print('Jack is ' + str(23) + ' years old.')


print(name + age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)
name_and_age = 'My name is {}. I\'m {} years old.'.format(23, "Jack")
print(name_and_age)
week_days = 'There are 7 days in a week: {mo}, {tu}, {we}, {th}, {fr}, {sa}, {su}.'\
     .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday', tu = 'Tuesday', fr = 'Friday', su = 'Sunday', sa ='Saturday')
print(week_days)
#
float_result = 1000/7
print(float_result)
print('The result is {0:10.3f}'.format(float_result))
print(('''
{0:5.2f}{1:10.2f}{2:10.2f}
{3:10.2f}{4:10.2f}{5:10.4f}
{6:10.2f}{7:10.2f}{8:10.2f}
'''.format(1.45645, 3535.45454, 5656.4, 45665.0, 45465.5, 454.4545, 564654.88, 4545.54, 454548.85)))

#
name_and_age_new = 'My name is {name}. I\'m {age} years old.'
print(name_and_age_new)
print('My name is %s. I\'m %d years old.' % (name, age)) #depricated
print('My name is %s. %s %d years old.' % (name, "I'm", age)) #depricated
f_number_00 = 5 / 16
f_number_01 = 100 / 7
f_number_02 = 1000 / 25
f_number_03 = 1000 / 2500
f_number_10 = 1000 / 250
f_number_11 = 100 / 128
f_number_12 = 1000 / 16
f_number_13 = 1000 / 64

print('''
{0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f}
{4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
'''.format(f_number_00, f_number_01, f_number_02, f_number_03,
           f_number_10, f_number_11, f_number_12, f_number_13))

print(f_number_00)
print(f_number_01)
print(f_number_02)
print(f_number_03)

print(f_number_10)
print(f_number_11)
print(f_number_12)
print(f_number_13)