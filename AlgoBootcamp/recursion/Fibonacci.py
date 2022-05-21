memoize = {0: 0, 1: 1}


def fib(n):
    if n not in memoize:
        result = fib(n - 1) + fib(n - 2)
        memoize[n] = result
    return memoize[n]

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n-1) + fib2(n-2)


print(fib(6))
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
