# https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                j = n - 1
                while j > i:
                    arr[j] = arr[j-1]
                    j -= 1
                i += 1
                if i < n:
                    arr[i] = 0
            i += 1