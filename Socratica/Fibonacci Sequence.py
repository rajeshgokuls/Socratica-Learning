
def fibonacci(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:

        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 101):
    print(n, ":", fibonacci(n))


#range function doesn't include final number
#this function calls itself, so we call as recursive function"""