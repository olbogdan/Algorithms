// Pyramid has spaces on both the left and right hand sides
// Examples
// pyramid(4)
// "   #   "
// "  ###  "
// " ##### "
// "#######"

fun main() {
    pyramid(4)
}

fun pyramid(levels: Int) {
    val levelSize = levels * 2 - 1
    for (i in 1.. levels) {
        val blocksAtCurrentLevel = i*2-1
        val border = (levelSize - blocksAtCurrentLevel) / 2
        println(" ".repeat(border)
                + "#".repeat(blocksAtCurrentLevel)
                + " ".repeat(border)
        )
    }
}
