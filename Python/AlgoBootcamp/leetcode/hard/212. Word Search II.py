# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once in a word.
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
from typing import List

# Solution 1

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


solution = Solution()
assert solution.findWords([["a","b"],["c","d"]], ["ab"]) == ["ab"]
assert solution.findWords([["a","b"],["c","d"]], ["ad"]) == []
result = solution.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"])
assert set(result).issubset({'oaa', 'oa'})


# Solution 2
class TrieNode2:
    def __init__(self):
        self.children = {}  # {letter, node}
        self.isEndOfWord = False
        self.refs = 0


class Trie2:
    def __init__(self):
        self.node = TrieNode2()

    def insert(self, word):
        curr = self.node
        curr.refs += 1
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode2()
            curr = curr.children[s]
            curr.refs += 1
        curr.isEndOfWord = True

    def remove(self, word):
        curr = self.node
        curr.refs -= 1
        for s in word:
            if s not in curr.children:
                break
            curr = curr.children[s]
            curr.refs -= 1

    def isWord(self, word):
        curr = self.node
        for s in word:
            if s not in curr.children or curr.children[s].refs <= 0:
                return False
            curr = curr.children[s]
        return curr.isEndOfWord

    def isPrefix(self, word):
        curr = self.node
        for s in word:
            if s not in curr.children or curr.children[s].refs <= 0:
                return False
            curr = curr.children[s]
        return True


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie2()
        for word in words:
            trie.insert(word)

        rowsLen = len(board)
        colLen = len(board[0])
        result = set()
        visited = set()
        currString = []

        def dfs(row, col):
            if row < 0 or row >= rowsLen or col < 0 or col >= colLen:
                return
            if len(words) == len(result):
                return
            node = (row, col)
            if node in visited:
                return
            s = board[row][col]
            tempStr = "".join(currString) + s
            if not trie.isPrefix(tempStr):
                return
            if trie.isWord(tempStr) and tempStr not in result:
                result.add(tempStr)
                trie.remove(tempStr)

            currString.append(s)
            visited.add((row, col))

            # check, left/right/down/up
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

            # remove from visited node
            # pop last char
            visited.remove((row, col))
            currString.pop()

        for row in range(rowsLen):
            for col in range(colLen):
                dfs(row, col)
        return list(result)


solution = Solution2()
result = solution.findWords([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"])
assert set(result).issubset({'oaa', 'oa'})
assert solution.findWords([["a","b"],["c","d"]], ["ab"]) == ["ab"]
assert solution.findWords([["a","b"],["c","d"]], ["ad"]) == []
