#CACHE -a collection of items of the same type stored in a hidden or inaccessible place.


fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n] #if we've cached the value, then return it

    if n == 1:    #compute the Nth term
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci_cache[n] = value  #cache the value and return it
    return value

for n in range(1, 10):
    print(n, ":", fibonacci(n))





