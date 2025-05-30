# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDist = 0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    maxDist = max(maxDist, j-i)
        return maxDist
