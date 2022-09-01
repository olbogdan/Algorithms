# Given an integer n, return the number of prime numbers that are strictly less than n.
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def countPrimes(n: int) -> int:
    if n <= 1:
        return 0

    arr = [1] * n
    arr[0] = 0
    arr[1] = 0

    i = 2
    while i * i < n:
        if arr[i] == 1:
            for j in range(i * i, n, i):
                arr[j] = 0
        i += 1

    return sum(arr)

assert countPrimes(10) == 4
assert countPrimes(2) == 0
assert countPrimes(3) == 1

