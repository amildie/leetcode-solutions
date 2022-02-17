# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occs = {}
        for n in nums:
            if n in occs.keys():
                return True
            else:
                occs[n] = True
        return False