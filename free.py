# array_size = 6
# array = [None for i in range(array_size)]
# print(array)

# array[0] = 'thanh'

# print(array)

list =[]
for i in range(int(input())):
    x = input()
    list.append(x)
list.reverse()
print(list)
for i in range(len(list)):
    print(list[i])
