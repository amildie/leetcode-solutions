// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let maxDiff = -1;
    for (i = 0; i < nums.length; ++i){
        for (j = i+1; j < nums.length; ++j) {
            if (nums[i] < nums[j]) {
                maxDiff = Math.max(maxDiff, nums[j]-nums[i]);
            }
        }
    }
    return maxDiff;
};
