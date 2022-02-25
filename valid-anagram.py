# https://leetcode.com/problems/valid-anagram/

class Solution:
    def buildOccs(self, s):
        occs = {}
        for c in s:
            if c in occs.keys():
                occs[c] = occs[c]+1
            else:
                occs[c] = 1
        return dict(sorted(occs.items()))

    def isAnagram(self, s: str, t: str) -> bool:
        sOccs = self.buildOccs(s)
        tOccs = self.buildOccs(t)
        return sOccs == tOccs