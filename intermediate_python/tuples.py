import sys

my_tuple =(['Max', 'Ronaldo', 'Messi'], 'Neyma')
my_tuple2 =('Ronaldo', 'Messi', "Mpabbe", 'Neyma', 'Lewandowski')
my_list = ['Ronaldo', 'Messi', "Mpabbe", 'Neyma', 'Lewandowski']
my_letters = ('p', 'h', 'j', 'u', 't', 'm', 'k')
my_numbers =(1, 5, 8, -2, 7, 9, 3, -5)

#we can use the element to get the index number
a = my_letters.index(('m'))
print(a)

#slicing, similar to list
b = my_numbers[::2]
print(b)

#destructuring
me, you, him, her, them = my_tuple2
print(me)
print(you)
print(him)
print(her)
print(them)

#using * to unpack a tuple and creating a list
i1, *i2, i3 = my_numbers
print(i1)
print(*i2)
print(i3)

#comparing a tuple and a list, tuple always has a smaller size, tuple is more efficient
print(sys.getsizeof(my_tuple2))
print(sys.getsizeof(my_list))

