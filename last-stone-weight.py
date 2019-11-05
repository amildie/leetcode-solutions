# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()
            s3 = s1-s2
            if s3 > 0:
                stones.append(s3)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
