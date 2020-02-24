#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        while(True):
            i = self.getDupIndex(S)
            if i == -1:
                return S
            S = S[:i] + S[i+2:]
        return S
    
    def getDupIndex(self, S: str) -> int:
        i = 0
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                return i
        return -1