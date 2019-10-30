# # https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for n in arr:
            k = str(n)
            if k in occ:
                occ[k] += 1
            else:
                occ[k] = 0
        
        vals = []
        for k, v in occ.items():
            if v in vals:
                return False
            else:
                vals.append(v)
        return True
