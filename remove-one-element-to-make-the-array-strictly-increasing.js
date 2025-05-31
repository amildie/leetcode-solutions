// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isIncreasing = function(nums) {
    for (let i = 0; i < nums.length-1; ++i) {
        if (nums[i] >= nums[i+1]) {
            return false;
        }
    }
    return true;
}

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canBeIncreasing = function(nums) {
    result = false;
    for (let i = 0; i < nums.length; ++i) {
        let tNums = nums.slice(0, i).concat(nums.slice(i + 1));
        if (isIncreasing(tNums)) {
            return true;
        }
    }
    return false;
};
