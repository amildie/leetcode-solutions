# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)/2
        occ = {}
        for a in A:
            if a in occ:
                occ[a] += 1
                if occ[a] == n:
                    return a
            else:
                occ[a] = 1
