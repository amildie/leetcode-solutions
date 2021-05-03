// https://leetcode.com/problems/height-checker

function heightChecker(heights: number[]): number {
  let res: number = 0;
  const sortedHeights: number[] = [... heights].sort((a,b) => (a-b));

  for (let i = 0; i < heights.length; ++i) {
    if (heights[i] != sortedHeights[i]) {
      res++;
    }
  }
  
  return res;
};