import Foundation

func fib(_ i: Int) -> Int {
    
    if i < 2 {
        return i
    }
    
    return fib(i-1) + fib(i-2)
}

print(fib(3))
