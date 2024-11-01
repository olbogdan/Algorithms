package leetcode.easy

class `1957 Delete Characters to Make Fancy String` {
    fun makeFancyString(s: String): String {
        val stack = StringBuilder()
        for (i in 0..<s.count()) {
            val sz = stack.count()
            val curChar = s[i]
            if (sz >= 2 && stack[sz-1] == curChar && stack[sz-2] == curChar) {
                continue
            }
            stack.append(curChar)
        }
        return stack.toString()
    }
}