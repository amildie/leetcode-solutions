# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _prod = 1
        _sum = 0
        for c in str(n):
            _prod = _prod * int(c)
            _sum = _sum + int(c)
        return _prod-_sum