// https://leetcode.com/problems/array-partition-i/

/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
  nums.sort((a, b) => b - a);
    
  let sum = 0;
  for(let i = 0; i < nums.length; i = i+2) {
    sum += Math.min(nums[i], nums[i+1]);
  }

  return sum;
};