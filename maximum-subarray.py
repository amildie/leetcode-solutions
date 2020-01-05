# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = [-1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                s[i] = nums[i]
            else:
                s[i] = max(nums[i], nums[i] + s[i-1])
        return max(s)