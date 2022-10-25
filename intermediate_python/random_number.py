import random
import secrets
import numpy as np

#number between 0 and 1
a = random.random()
#number between a range
b = random.randrange(1,10)

#random choice on anything
l = 'ABFGHRGH'
c = random.choice(l)

# randome sample group of a list
d = random.sample(l, 3)

#shuffle a list
random.shuffle(list(l))


#secrets for password,security tokens
f = secrets.randbelow(10)
g = secrets.randbits(4)
h = secrets.choice(l)



#numpy
i = np.random.rand(3,3)
j = np.random.randint(1,100,3)

print(i)