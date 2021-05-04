// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order

function minSubsequence(nums: number[]): number[] {
  nums.sort((a,b) => (b-a));
  let res: number[] = nums;
  let minLength = res.length;

  for (let i = 0; i < nums.length; ++i) {
    const numsL = nums.slice(0, i+1);
    const numsR = nums.slice(i+1, nums.length);
    const numsLsum = numsL.reduce((a,b) => a+b, 0);
    const numsRsum = numsR.reduce((a,b) => a+b, 0);

    if (numsLsum > numsRsum && numsL.length < minLength) {
      res = numsL;
      minLength = numsL.length;
    }
  }

  return res;
};