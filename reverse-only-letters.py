# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = []
        for c in S:
            if c.isalpha():
                letters.append(c)
        i = 0
        arr = list(S)
        letters.reverse() 
        for j in range(len(arr)):
            if arr[j].isalpha():
                arr[j] = letters[i]
                i += 1
        return ''.join(arr)