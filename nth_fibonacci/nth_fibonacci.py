
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

def fib3(n):
    lastTwo = [0, 1]
    counter = 2
    while counter < n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1]

print(fib1(9))
print(fib2(9))
print(fib3(9))