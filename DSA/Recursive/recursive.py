# Iteration version

def sum_to_one(n):
    result = 0
    for n in range(n, 0, -1):
        result += n
    print(result)
sum_to_one(4)

#Recursive version
def sum_to_one_recrusive(n):
    if n == 1: # this is the base case
        return n
    print('Recursing with input: {0}'.format(n))
    return n + sum_to_one_recrusive(n-1)
print(sum_to_one_recrusive(7))

#This is what happened with n = 7
# sum_to_one_recrusive(7) = n + sum_to_one_recrusive(n-1) 
# = 7 + sum_to_one_recrusive(6) = 7 + (6 + sum_to_one_recrusive(5))= 7 + 6 + (5 + sum_to_one_recrusive(4)) =....
# = 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28  
