# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        occs = {}
        for n in nums:
            occs[n] = True
        for n in range(1, len(nums)+1):
            if n not in occs:
                res.append(n)
        return res