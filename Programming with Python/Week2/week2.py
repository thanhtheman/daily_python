#FUNCTION

# def calculate_tax(income,tax_rate):
#     total_tax = tax_rate * income
#     return total_tax

# print(calculate_tax(1000, 0.35))

#VARIABLE SCOPE

my_global = 10

# def fn1():
#     enclosed_v = 8
#     def fn2():
#         local_v = 5
#         print('Access my gloabl variable ', my_global)
#         print('Access my enclosed variable ', enclosed_v)
#     fn2()

# fn1()

#LIST
# list = [1, 2, 3]
# # print(list[-1])
# # print(*list)
# # print(list, sep = " ")
# list.append(5)
# list.insert(3, 6)
# list.pop(1)
# list.extend([8, 12, 213])
# del list[-1]
# for i in list:
#     print('Value is ', i**2)

#TUPLE
# my_tuple = (1, 2, 'hello', 4.56)
# print(type(my_tuple[2]))

#SETS
# set_a = {1, 2 ,3, 4, 5}
# set_b = {4, 5, 6, 7, 8, 9}

# print(set_a | set_b)
# print(set_a & set_b)
# print(set_a - set_b)
# print(set_a ^ set_b)

#DICTIONARY
# my_dic = {1: 'coffee', 3: 'car', 'name': 'thanh'}
# my_dic['job'] = {'software developer': 'backend'}
# print(my_dic)
# for a, b in my_dic.items():
#     print(str(a), ' and ', b)

#args and kwargs
# def sum(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum
# print(sum(4,5,6))

# def sum(**kwargs):
#     sum = 0
#     for key, value in kwargs.items():
#         sum += value
#     return round(sum, 2)
# print(sum(coffee=4, cake=5.2, coke=6.89))



menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

order = [{'name': 'espresso','price': 1.99}, {'name': 'coffee', "price": 2.50}, {"name": 'cake', "price": 2.79}]

subtotal = 0
for i in range(len(order)):
    subtotal += order[i]['price']
print(subtotal)

tax = subtotal * 0.15
print(float(round(tax, 2)))

