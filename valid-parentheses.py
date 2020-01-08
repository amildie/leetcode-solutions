# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        t = s
        while True:
            s = t
            t = t.replace("()", "")
            if t != s:
                continue
            t = t.replace("[]", "")    
            if t != s:
                continue
            t = t.replace("{}", "")
            if t != s:
                continue
            break
        if t == "":
            return True
        return False