# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = ''.join(sorted(text))
        res = 10001
        for c in ['b', 'a', 'll', 'oo', 'n']:
            if text.count(c) < res:
                res = text.count(c)
        return res