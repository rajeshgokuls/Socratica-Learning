from functools import lru_cache
print(dir(lru_cache)) #sometimes import function is not working

@lru_cache(maxsize= 1000)

def fibonacci(n):
 if type(n) != int:
     raise TypeError("n must be a positive int")
 if n < 1:
     raise ValueError("n must be a positive int")
 if n == 1:
        return 1
 elif n==2:
        return 1
 elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range(1, 1001):
    print(fibonacci(n+1)/fibonacci(n))




