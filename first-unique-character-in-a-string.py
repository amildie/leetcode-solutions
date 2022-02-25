# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        occs = {}
        for c in s:
            if c in occs.keys():
                occs[c] = occs[c]+1
            else:
                occs[c] = 1
        for c in occs.keys():
            if occs[c] == 1:
                return s.find(c)
        return -1