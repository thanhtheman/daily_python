# list =[]
# for i in range(int(input())):
#     x = input()
#     list.append(x)
# list.reverse()
for i in range(len(list)):
    print(list[i])

# the cool way
list =[]
for i in range(int(input())):
    x = input()
    list.append(x)
list = list[::-1]
print(*list)