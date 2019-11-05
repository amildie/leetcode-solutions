# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        for n in nums:
            if n in occ:
                occ[n] += 1
            else:
                occ[n] = 1
        for k, v in occ.items():
            if v >= len(nums)/2:
                return k
