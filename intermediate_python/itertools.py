#itertools: product = iterate to create all possible combinations of 2 arrays
#permuations = combining all possible mix and match in 1 array 
# combinations, accumulate, groupby and infinite iterators

from itertools import product, permutations, combinations, combinations_with_replacement,accumulate, groupby
import operator

a = [1, 2, 3]
b = [3, 4]
# prod = product(a,b)
# prod2 = product(a,b, repeat=2)
# print(list(prod))
# print(list(prod2))

# perm = permutations(a, 3)
# print(list(perm))

c = [1, 2, 3, 4]
# comb = combinations(a,2)
# comb2 = combinations_with_replacement(a,2)
# print(list(comb))
# print(list(comb2))

# accu = accumulate(c)
# accumul = accumulate(c, func=operator.mul)
# print(list(accu))
# print(list(accumul))

def smaller_than_3(x):
    return x < 3

group_obj = groupby(c, key=smaller_than_3)
# print(list(group_obj))

for key, value in group_obj:
    print(key, list(value))