import Foundation

var memoize = [0:0, 1:1]

func fib(_ n: Int) -> Int {
    if memoize[n] == nil {
        let result = fib(n-1) + fib(n-2)
        memoize[n] = result
    }
    return memoize[n]!
}

print(fib(3))
assert(fib(3) == 2)
assert(fib(4) == 3)
assert(fib(5) == 5)

