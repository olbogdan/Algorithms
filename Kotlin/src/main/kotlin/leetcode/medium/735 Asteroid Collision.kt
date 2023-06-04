package leetcode.medium
/*We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0*/

class `735 Asteroid Collision` {
    fun asteroidCollision(asteroids: IntArray): IntArray {
        val stack = mutableListOf<Int>()
        for (a in asteroids) {
            var asteroid = a
            while (stack.isNotEmpty() && stack.last() > 0 && asteroid < 0) {
                if (stack.last() < Math.abs(asteroid)) {
                    stack.removeAt(stack.lastIndex)
                } else if (stack.last() == Math.abs(asteroid)) {
                    stack.removeAt(stack.lastIndex)
                    asteroid = 0
                } else {
                    asteroid = 0
                }
            }
            if (asteroid != 0) {
                stack.add(asteroid)
            }
        }
        return stack.toIntArray()
    }
}


fun main() {
    val solution = `735 Asteroid Collision`()
    val input1 = intArrayOf(5, 10, -5)
    val output1 = intArrayOf(5, 10)
    assert(solution.asteroidCollision(input1).contentEquals(output1))
    val input2 = intArrayOf(8, -8)
    val output2 = intArrayOf()
    assert(solution.asteroidCollision(input2).contentEquals(output2))
}