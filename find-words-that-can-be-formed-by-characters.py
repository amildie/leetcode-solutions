# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def buildCharMap(self, chars: str) -> dict[str, int]:
        charMap = {}
        for c in chars:
            if c not in charMap:
                charMap[c] = 1
            else:
                charMap[c] += 1
        return charMap
    
    def isGood(self, globalCharMap: dict[str, int], wCharMap: dict[str, int]):
        for key, value in wCharMap.items():
            if key not in globalCharMap:
                return False
            else:
                if value > globalCharMap[key]:
                    return False
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        globalCharMap = self.buildCharMap(chars)
        for w in words:
            wCharMap = self.buildCharMap(w)
            if self.isGood(globalCharMap, wCharMap):
                res += len(w)
        return res
    