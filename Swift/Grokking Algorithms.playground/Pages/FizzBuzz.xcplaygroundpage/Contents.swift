import Foundation

func fizzBuzz(_ i: Int) {
    
    for i in 0..<i {
        switch (i%3 == 0, i%5 == 0) {
        case (true, true):
            print("FizzBuzz")
        case (false, true):
            print("Buzz")
        case (true, false):
            print("Fizz")
        default:
            print(i)
        }
    }
}

fizzBuzz(20)


