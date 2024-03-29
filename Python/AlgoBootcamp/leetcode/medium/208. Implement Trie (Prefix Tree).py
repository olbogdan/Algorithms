# A trie (pronounced as "try") or prefix tree is a tree data structure used
# to efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        return True


obj = Trie()
obj.insert("apple")
assert obj.search("apple") is True
assert obj.startsWith("app") is True
assert obj.startsWith("ple") is False


class Trie2:

    def __init__(self):
        self.words = set()
        self.prefixes = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

        for i in range(len(word)):
            self.prefixes.add(word[:i + 1])

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixes


obj = Trie2()
obj.insert("apple")
assert obj.search("apple") is True
assert obj.startsWith("app") is True
assert obj.startsWith("ple") is False
