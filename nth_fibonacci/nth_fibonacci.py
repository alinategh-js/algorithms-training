from math import sqrt

# time: O(2^n) | space: O(n)
def fib1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

# time: O(n) | space: O(n)
def fib2(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib2(n-1, memoize) + fib2(n-2, memoize)
        return memoize[n]

# time: O(n) | space: O(1)
def fib3(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        lastTwo = [0, 1]
        counter = 2
        while counter < n:
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextFib
            counter += 1
        return lastTwo[1]

def fib4(n):
    # using fibonacci's proven constant time formula
    n = n-1 # n starts from zero in this formula
    res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    return int(res)


print(fib1(9))
print(fib2(9))
print(fib3(9))
print(fib4(9))