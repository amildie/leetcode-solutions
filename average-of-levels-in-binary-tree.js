// https://leetcode.com/problems/average-of-levels-in-binary-tree/

/**
* Definition for a binary tree node.
* function TreeNode(val) {
*     this.val = val;
*     this.left = this.right = null;
* }
*/
/**
* @param {TreeNode} root
* @return {number[]}
*/
var averageOfLevels = function(root) {
  let map = {};
  addNodeVal(root, 0, map);
  
  let avgs = [];
  for(let key in map) {
    avgs[key] = (map[key].reduce((a, b) => a + b, 0))/map[key].length;
  }
  
  return avgs;
};

function addNodeVal(node, level, map) {
  if(!map[level]) {
    map[level] = [];
  }
  
  map[level].push(node.val);
  
  if(node.left) {
    addNodeVal(node.left, level+1, map);
  }
  if(node.right) {
    addNodeVal(node.right, level+1, map);
  }
}