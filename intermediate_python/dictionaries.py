my_dict =dict(name='Ronaldo', country='Portugal', age=38, club='Manchester United')
my_dict2 = dict(wife='model1', wife2='model2')

#destructuing or unpack a dict:
# a, b, *c = my_dict.values()
# print(a, b, c)

#delete a key-value paid
# # del my_dict['name']
# my_dict.popitem()
# print(my_dict)

#loop over the dictionary:

# for i in my_dict.keys():
#     print(f'This is my key: {i}')

# for key, value in my_dict.items():
#     print(key, value)

#copy a dictionary
# mydict_copy = my_dict.copy()
# mydict_copy['email'] ='cr7@cr7.com'
# print(my_dict)
# print(mydict_copy)

#merge 2 dictionaries
my_dict.update(my_dict2)
print(my_dict)
