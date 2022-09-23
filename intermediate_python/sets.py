# a set can't have duplicate value, so one 'l' has been eliminated 
# my_set = set('Hello')
# print(my_set)

#adding to a set
# my_set = set()
# my_set.add(1)
# my_set.add(2)
# my_set.add(1)
# my_set.add('Messi')
# print(my_set)

#remove the 1st element
# print(my_set.pop())

#union = combining without duplication and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
strings = {'Messi', 'Ronaldo', 'Neyma'}
primes = {2, 3, 5, 7}
sub_set = {3, 5, 7}

# u = odds.union(strings)
# i = odds.intersection(primes)
# print(i)
# print(u)

#differrence between 2 sets, only difference from odds, not on primes, that's why we don't have '2'
# d = odds.difference(primes)
# print(d)

#symmetric_difference, difference in both sets, now we get the element '2'
# diff = odds.symmetric_difference(primes)
# print(diff)

#subset
print(sub_set.issubset(odds))
print(odds.issuperset(sub_set))