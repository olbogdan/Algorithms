/// Write a function that accepts a positive namber N.
/// The function should console log a step shape with N levels
/// using the # character. The step has spaces on the right hand side!
/// example
/// steps(3)
/// "#   "
/// "## "
/// "###"

fun steps(n: Int) {
    val listSteps = MutableList(n) { " " }
    for (i in 0 until n) {
        listSteps[i] = "#"
        println(listSteps.joinToString(""))
    }
}

fun steps2(n: Int) {
    fun rec(step: Int) {
        if (step < 0) {
            return
        }
        val stair = n - step
        println("#".repeat(stair) + " ".repeat(step))
        rec(step-1)
    }
    rec(n)
}

fun main() {
    steps(3)
    steps2(3)
}