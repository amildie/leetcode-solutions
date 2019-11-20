# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        minAbsDiff = 100**100
        arr.sort()
        for i in range(len(arr)-1):
            t = arr[i+1]-arr[i]
            if t < minAbsDiff:
                minAbsDiff = t
                res = [[arr[i],arr[i+1]]]
            elif t == minAbsDiff:
                res.append([arr[i],arr[i+1]])
        return res
