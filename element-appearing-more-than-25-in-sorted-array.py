# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        i = 0
        while i < n:
            j = 1
            while i+j < n and arr[i] == arr[i+j]:    
                j+=1
                if j > n/4:
                    return arr[i]
            i = i+j