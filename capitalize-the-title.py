# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = ""
        words = title.split()
        for word in words:
            t = word.lower()
            if len(word) > 2:
                t = t.capitalize()
            t += " "
            res += t
        return res.rstrip()