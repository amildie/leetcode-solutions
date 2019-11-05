# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        Ao = []
        Ae = []
        for a in A:
            if a%2 == 0:
                Ae.append(a)
            else:
                Ao.append(a)
        res = []
        for i in range(len(Ao)):
            res.append(Ae[i])
            res.append(Ao[i])
        return res
