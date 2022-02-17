# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        leafHeights = []
        if root.left:
            self.findLeaf(root.left, 1, leafHeights)
        if root.right:
            self.findLeaf(root.right, 1, leafHeights)
        return min(leafHeights)

    def findLeaf(self, node, height, leafHeights):
        if node.left == None and node.right == None:
            leafHeights.append(height+1)
        else:
            if node.left:
                self.findLeaf(node.left, height+1, leafHeights)
            if node.right:
                self.findLeaf(node.right, height+1, leafHeights)