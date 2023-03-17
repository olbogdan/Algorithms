import org.junit.jupiter.api.Assertions

fun fib(n: Int): Int {
    if (n < 2) {
        return n
    }

    var prev = 0
    var current = 1
    for (i in 2 .. n) {
        val nextValue = prev + current
        prev = current
        current = nextValue
    }
    return current
}

var memoize = mutableMapOf<Int, Int>(0 to 0, 1 to 1)
fun fibRecursion(n: Int): Int {
    if (memoize[n] == null) {
        val result = fibRecursion(n-1) + fibRecursion(n-2)
        memoize[n] = result
        return result
    }
    return memoize[n]!!
}

fun main() {
    Assertions.assertTrue(fib(9) == 34)
    Assertions.assertTrue(fib(1) == 1)
    Assertions.assertTrue(fib(2) == 1)

    Assertions.assertTrue(fibRecursion(9) == 34)
    Assertions.assertTrue(fibRecursion(1) == 1)
    Assertions.assertTrue(fibRecursion(2) == 1)

    println(fibRecursion(0))
    println(fibRecursion(1))
    println(fibRecursion(2))
    println(fibRecursion(3))
    println(fibRecursion(4))
    println(fibRecursion(5))
    println(fibRecursion(6))
    println(fibRecursion(7))
    println(fibRecursion(8))
    println(fibRecursion(9))

    println(fib(0))
    println(fib(1))
    println(fib(2))
    println(fib(3))
    println(fib(4))
    println(fib(5))
    println(fib(6))
    println(fib(7))
    println(fib(8))
    println(fib(9))
}
