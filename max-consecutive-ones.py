# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _nums = ''.join(str(n) for n in nums)
        _nums = _nums.split("0")
        res = 0
        for n in _nums:
            if len(n) > res:
                res = len(n)
        return res