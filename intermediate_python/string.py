#string is like list
my_string = 'Hello The Fucking World'
# print(my_string[0])

#substring - just like a list
# print(my_string[1:25:2])

#add string with just '+'
name = 'My name is Thanh'
# print(name + my_string)

#get rid of space
# no_space = my_string.strip()
# upper = my_string.upper()
# print(upper)

#find an index number
# find_index = my_string.find('e')
# print(find_index)

#convert a string to a list
# my_list = my_string.split()
# print(my_list)

#convert a list to a string,a  very useful method
# new_string = ' '.join(my_list)
# print(new_string)

#format a string $, .format(), f-string
x = 3.123
y = 12.3636
my_string2 = 'This is a variable %f' % x
my_string3 = 'This is a variable {} and {}'.format(x, y)
print(my_string3)
my_string4 = f'This is a variable {x} and {y}'
print(my_string4)