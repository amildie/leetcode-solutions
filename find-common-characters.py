# https://leetcode.com/problems/find-common-characters/

class Solution:    
    def commonChars(self, A: List[str]) -> List[str]:
        letters = set(A[0])
        occs = {}
        for l in letters:
            occs[l] = 101
            for a in A:
                if a.count(l) < occs[l]:
                    occs[l] = a.count(l)
        res = []
        for l in letters:
            for _ in range(occs[l]):
                res.append(l)
        return res