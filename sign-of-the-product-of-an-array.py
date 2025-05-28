class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for n in nums:
            if n == 0:
                return 0
            p *= n
        if p < 0:
            return -1
        else:
            return 1
