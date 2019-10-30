# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        aE = []
        aO = []
        for n in A:
            if n % 2 == 0:
                aE.append(n)
            else:
                aO.append(n)
        return aE + aO

