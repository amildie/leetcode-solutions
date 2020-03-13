# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = A.copy()
        B.sort()
        C = B.copy()
        C.reverse()
        if A == B or A == C:
            return True
        return False