import org.junit.jupiter.api.Assertions.*

fun anagrams(str1: String, str2: String): Boolean {
    val plainStr1 = str1.filter { it.isLetterOrDigit() }.lowercase()
    val plainStr2 = str2.filter { it.isLetterOrDigit() }.lowercase()

    val strMap1 = HashMap<Char, Int>()
    plainStr1.forEach {
        val count = strMap1[it] ?: 0
        strMap1[it] = count + 1
    }
    val strMap2 = HashMap<Char, Int>()
    plainStr2.forEach {
        val count = strMap2[it] ?: 0
        strMap2[it] = count + 1
    }

    return strMap1 == strMap2
}

fun anagrams2(str1: String, str2: String): Boolean {
    val plainStr1 = str1.filter { it.isLetterOrDigit() }.lowercase()
    val plainStr2 = str2.filter { it.isLetterOrDigit() }.lowercase()
    return plainStr1.toCharArray().sorted() == plainStr2.toCharArray().sorted()
}

fun main() {
    println(anagrams("b a3Bx!", ",  3babx"))

    assertTrue(anagrams("aba   ", "baa!"))
    assertFalse(anagrams("ab", "baa"))
    assertFalse(anagrams("baa", "ab"))

    println(anagrams2("b a3Bx!", ",  3babx"))

    assertTrue(anagrams2("aba   ", "baa!"))
    assertFalse(anagrams2("ab", "baa"))
    assertFalse(anagrams2("baa", "ab"))
}