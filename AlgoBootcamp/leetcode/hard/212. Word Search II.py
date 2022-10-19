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


class TrieNode:
    def __init__(self):
        self.children = {}  # {letter, node}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word):
        curr = self.node
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.isEndOfWord = True

    def isWord(self, word):
        curr = self.node
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.isEndOfWord

    def isPrefix(self, word):
        curr = self.node
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rowsLen = len(board)
        colLen = len(board[0])
        result = []
        visited = set()
        currString = []

        def dfs(row, col):
            if row < 0 or row >= rowsLen or col < 0 or col >= colLen:
                return
            node = (row, col)
            if node in visited:
                return
            s = board[row][col]
            currString.append(s)
            tempStr = "".join(currString)
            if not trie.isPrefix(tempStr):
                return
            if trie.isWord(tempStr):
                result.append(tempStr)

            visited.add((row, col))

            # check, left/right/down/up
            # dfs(row - 1, col)
            dfs(row + 1, col)
            # dfs(row, col - 1)
            dfs(row, col + 1)

            # remove from visited node
            # pop last char
            visited.remove((row, col))
            currString.pop()

        for row in range(rowsLen):
            for col in range(colLen):
                dfs(row, col)
        return result


solution = Solution()
print(solution.findWords([["a","b"],["c","d"]], ["ab"]))