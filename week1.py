#CONTROL FLOW

# billTotal = float(input())
# discount = 0.1
# discount2 = 0.2

# if billTotal > 100 and billTotal < 200:
#     print('Bill > 100, 10% discount is applied')
#     discountAmount = discount * billTotal
#     print('Discount Amount = '+ str(discountAmount))
#     billTotal = billTotal - discountAmount
# elif billTotal >= 200:
#     print('Bill > 200, 20% discount is applied')
#     discountAmount = discount2 * billTotal
#     print('Discount Amount = '+ str(discountAmount))
#     billTotal -= discountAmount
# else:
#     print('Bill is less than 100!') 

# print('Total bill $' + str(billTotal))

# http_status = 701
# match http_status:
#     case 200 | 201:
#         print('Success')
#     case 400:
#         print('Bad request')
#     case 500 | 501:
#         print('Server Error')
#     case _:
#         print('Unknown')


#LOOPING

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']
# for idx, item in enumerate(favorites):
#     print(idx, item)

# count = 0
# while count < len(favorites):
#     print('I like dessert:', favorites[count])
#     count += 1

#CONDITIONAL LOOPING

# for i in favorites:
#     if i == 'Apple Pie':
#         print('We have your favorite desser')
#         break
# else:
#     print("Sorry, we don't have it")

# for i in favorites:
#     if i == 'Apple Pie':
#         print('We have your favorite desser')
#         continue
#     print("Sorry, we don't have it")

# for i in favorites:
#     if i == 'Apple Pie':
#         pass
#     print("Yes, we have our favorite desert", i)

#NESTED LOOPS
# import time
# start_time = time.time()

# for i in range(10):
#     print("0", end = " ")
#     for j in range(10):
#         print("#", end = " ")
#     print()
# print(round((time.time() - start_time), 2))

list = []
for i in range(5):
    list.append(i)
print(list)
for j in list:
    print(j**2)