my_list = ['apple', 'banana', 5, True, 4, 8, 'lamboghini']
int_list = [1, 2, 4, 8, 3, 7, -1, -5, -3]

#jumping position [start:end:step to jump], starting from index 0  to end, jump 2 steps in between
# #[1, 4, 3, -1, -3]
a = int_list[0::2]
print(a)

#using this technique to reverse a list, "-1" means go back 1 position.
b = int_list[::-1]
print(b)

#create a new copy of a list so that the original list is not affected
copy_list = my_list.copy()
copy_list.append('watermelon')
print(my_list)

#a shortcut to loop over your list [expression + for loop]
c = [i*i for i in int_list]
print(c)

