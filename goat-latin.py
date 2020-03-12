# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = ""
        words = S.split(" ")
        i = 1
        for w in words:
            if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                t = w + "ma"
            else:
                t = w[1:] + w[0] + "ma"
            t = t + 'a' * i + " "
            res = res + t
            i+=1
        return res[:-1]