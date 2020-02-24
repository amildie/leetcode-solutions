# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        resp = []
        for n in range(left, right+1):
            if self.isSelfDividing(n):
                resp.append(n)
        return resp
    
    def isSelfDividing(self, n: int) -> bool:
        s = str(n)
        if '0' in s:
            return False
        for c in s:
            if n % int(c) != 0:
                return False
        return True