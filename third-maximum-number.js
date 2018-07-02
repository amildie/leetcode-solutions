// https://leetcode.com/problems/third-maximum-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
  let firstMax = Math.max.apply(null, nums);
  nums = nums.filter(n => n !== firstMax);

  let secondMax = Math.max.apply(null, nums);
  nums = nums.filter(n => n !== secondMax);

  if(nums.length > 0) {
    return Math.max.apply(null, nums);
  }

  return firstMax;
};