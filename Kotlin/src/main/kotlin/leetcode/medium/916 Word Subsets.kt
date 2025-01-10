package leetcode.medium

import kotlin.test.assertEquals

class `916 Word Subsets` {
    fun getCount(word: String): Map<Char, Int> {
        val tempCollect = HashMap<Char, Int>()
        for (i in 0..<word.count()) {
            tempCollect[word[i]] = tempCollect.getOrDefault(word[i], 0) + 1
        }
        return tempCollect
    }
    fun wordSubsets(words1: Array<String>, words2: Array<String>): List<String> {
        val collect = HashMap<Char, Int>()
        for (i in 0..<words2.count()) {
            val word = words2[i]
            val tempCollect = getCount(word)
            tempCollect.forEach { key, value ->
                if (collect.getOrDefault(key, 0) < value) {
                    collect[key] = value
                }
            }
        }
        val res = ArrayList<String>()
        words1.forEach { word ->
            val universal = getCount(word)
            var candidate = true
            for (key in collect.keys) {
                if (collect.getOrDefault(key, 0) > universal.getOrDefault(key, 0)) {
                    candidate = false
                    break
                }
            }
            if (candidate) {
                res.add(word)
            }
        }
        return res
    }
}


fun main() {
    val res = `916 Word Subsets`().wordSubsets(arrayOf("amazon","apple","facebook","google","leetcode"), arrayOf("e","oo"))
    assertEquals(listOf("facebook","google"), res)
}