# https://leetcode.com/problems/keyboard-row/

class Solution:
    def allInRow(self, word, row) -> bool:
        for l in word:
            if l.lower() not in row:
                return False
        return True

    def findWords(self, words: List[str]) -> List[str]:
        row0 = "qwertyuiop"
        row1 = "asdfghjkl"
        row2 = "zxcvbnm"
        res = []
        for word in words:
            if self.allInRow(word, row0) or self.allInRow(word, row1) or self.allInRow(word, row2):
                res.append(word)
        return res