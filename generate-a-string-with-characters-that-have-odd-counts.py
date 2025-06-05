# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        res = ""
        if n == 1:
            return "a"
        if n % 2 == 0:
            res = "a" * (n-1)
            res += "b"
        else:
            res = "a" * (n-2)
            res += "bc"
        return res
