#collections are containers: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter

a ='aaaaaaabbbbbccccc'
my_counter = Counter(a)

print(my_counter)
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0][1])
# print(list(my_counter.elements()))
print(my_counter.keys())
print(list(my_counter.values())[0])

