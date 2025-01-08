package leetcode.easy

class `3042 Count Prefix and Suffix Pairs I` {
    fun countPrefixSuffixPairs(words: Array<String>): Int {
        var res = 0
        val N = words.count()
        for (i in 0..<N) {
            for (j in i+1..<N) {
                val w1 = words[i]
                val w2 = words[j]
                val len1 = w1.count()
                val len2 = w2.count()
                if (len2 < len1) {
                    continue
                }
                val substring = w2.substring(0, len1)
                val substring1 = w2.substring(len2 - len1, len2)
                if (substring == w1 && substring1 == w1) {
                    res++
                }
            }
        }
        return res
    }
}


fun main() {
    val res = `3042 Count Prefix and Suffix Pairs I`().countPrefixSuffixPairs(arrayOf("a","aba","ababa","aa"))
    println(res)
}