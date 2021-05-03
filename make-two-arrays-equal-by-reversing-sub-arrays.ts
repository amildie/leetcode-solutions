// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays

function canBeEqual(target: number[], arr: number[]): boolean {
  return JSON.stringify(target.sort()) === JSON.stringify(arr.sort());
};