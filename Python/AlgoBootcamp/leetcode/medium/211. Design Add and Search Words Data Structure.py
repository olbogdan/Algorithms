#Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.contains(word, cur)

    def contains(self, word, node: TrieNode) -> bool:
        if not word:
            if node.endOfWord:
                return True
            else:
                return False

        if word[0] != ".":
            if word[0] in node.children:
                _node = node.children[word[0]]
                return self.contains(word[1:], _node)
            else:
                return False
        else:
            for val in node.children.values():
                if self.contains(word[1:], val):
                    return True
            return False


obj = WordDictionary()
obj.addWord("WordDictionary")
obj.addWord("word")
assert obj.search("word") is True
assert obj.search("WordDictionary") is True
assert obj.search("WordDi") is False
assert obj.search(".or.") is True
assert obj.search("....") is True
