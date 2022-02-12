# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._postorderTraversal(root)
    
    def _postorderTraversal(self, node) -> List[int]:
        if node == None:
            return []
        else:
            return self._postorderTraversal(node.left) + self._postorderTraversal(node.right) + [node.val]
