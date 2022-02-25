# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxs = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in idxs:
                idxs[n].append(i)
            else:
                idxs[n] = [i]
            
        for i in range(len(nums)):
            idx = idxs[nums[i]] 
            if len(idx) > 1:
                idx.remove(i)
                if abs(i-idx[0]) <= k:
                    return True

        return False