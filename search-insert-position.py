# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[0] > target:
                return 0
            if nums[i] == target:
                return i
            if nums[i] < target:
                if i == len(nums)-1 or target < nums[i+1]:
                    return i+1