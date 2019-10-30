# https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    def rangeSumBSTr(self, node: TreeNode, L: int, R: int, nums: List[int]) -> int:
        if node == None:
            return
        if node.val >= L and node.val <= R:
            nums.append(node.val)
        self.rangeSumBSTr(node.left, L, R, nums)
        self.rangeSumBSTr(node.right, L, R, nums)

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        arr = []
        self.rangeSumBSTr(root, L, R, arr)
        return sum(arr)
