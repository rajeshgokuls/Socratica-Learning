# Test all divisors from 2 thru sqrt(N)
import math
import time

print(dir(math))
print(dir(time))

# def is_prime_v1(n):
#
#     if n ==1:
#         return False # 1 is not prime
#     for d in range(2, n):
#         if n % d == 0:
#             return False
#     return True

def is_prime_v2(n):

    """Return 'True' if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False #1 is not prime


    max_divisor = math.floor(math.sqrt(n))#math.floor will round down the number to the closest digit

    for d in range(2,  max_divisor):  #add one to the range function, # without adding 1+ it will stop at 36 square root
        if n % d == 0:
            return False
    return True

for n in range(1, 21):
    print(n, is_prime_v2(n))

# to print only prime numbers use the below code

    # if(is_prime_v2(n) == True):
    #     print(n)













