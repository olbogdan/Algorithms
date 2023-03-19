package leetcode.medium

import kotlin.test.assertFails
import kotlin.test.assertFalse
import kotlin.test.assertTrue

/*Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.*/
class TrieNode {
    val children = mutableMapOf<Char, TrieNode>()
    var isEndOfWord = false
}

class WordDictionary() {

    private val root = TrieNode()

    fun addWord(word: String) {
        var node = root
        for (c in word) {
            if (!node.children.containsKey(c)) {
                node.children[c] = TrieNode()
            }
            node = node.children[c]!!
        }
        node.isEndOfWord = true
    }

    fun search(word: String): Boolean {
        return searchInNode(root, word)
    }

    private fun searchInNode(node: TrieNode, word: String): Boolean {
        if (word.isEmpty()) {
            return node.isEndOfWord
        }
        val c = word[0]
        if (c != '.') {
            if (!node.children.containsKey(c)) {
                return false
            }
            return searchInNode(node.children[c]!!, word.substring(1))
        } else {
            for (child in node.children.values) {
                if (searchInNode(child, word.substring(1))) {
                    return true
                }
            }
            return false
        }
    }
}

fun main() {
    val wordDictionary = WordDictionary()
    wordDictionary.addWord("abc")
    wordDictionary.addWord("def")
    wordDictionary.addWord("ghi")
    assertFalse(wordDictionary.search("jkl"))
    assertTrue(wordDictionary.search("d.f"))
}