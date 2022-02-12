# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._inorderTraversal(root)
    
    def _inorderTraversal(self, node) -> List[int]:
        if node == None:
            return []
        else:
            return self._inorderTraversal(node.left) + [node.val] + self._inorderTraversal(node.right)
