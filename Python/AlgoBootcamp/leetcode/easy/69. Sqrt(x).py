# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1

    low = 0
    high = x
    while low + 1 < high:
        mid = low + (high - low) // 2
        square = mid * mid
        if square == x:
            return int(mid)
        if square < x:
            low = mid
        if square > x:
            high = mid

    return int(low)

assert mySqrt(5) == 2
assert mySqrt(4) == 2
assert mySqrt(3) == 1
assert mySqrt(16) == 4