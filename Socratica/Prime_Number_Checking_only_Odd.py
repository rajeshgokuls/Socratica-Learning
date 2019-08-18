# Test all divisors from 2 thru sqrt(N)
import math
import time

print(dir(math))
print(dir(time))

def is_prime_v3(n):

    """Return 'True' if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False #1 is not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False  #value is not prime, so return false

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3,  1 + max_divisor, 2 ): #here 2 is a step -value,without 2 the program will still work well
        if n % d == 0:
            return False
    return True


#==========Test Function =========
for n in range(1, 21):
    print(n, is_prime_v3(n))















