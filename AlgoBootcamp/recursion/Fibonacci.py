memoize = {0: 0, 1: 1}


def fib(n):
    if n not in memoize:
        result = fib(n - 1) + fib(n - 2)
        memoize[n] = result
    return memoize[n]


print(fib(6))
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
