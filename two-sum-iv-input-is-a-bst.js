// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function(root, k) {
  return checkNode(root, k, []);
};

function checkNode(node, k, foundNodes) {
  if(!node) {
      return false;
  }
    
  if(foundNodes.includes(k - node.val)) {
    return true;
  } else {
    foundNodes.push(node.val);
    return(checkNode(node.left, k, foundNodes) || checkNode(node.right, k, foundNodes));
  }
}