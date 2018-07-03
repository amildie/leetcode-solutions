// https://leetcode.com/problems/min-cost-climbing-stairs/

/**
* @param {number[]} cost
* @return {number}
*/
function minCostFrom(step, costs) {
  if(M[step] !== -1) {
    return M[step];
  }

  let stepCost = costs[step];

  if(step === costs.length-1 || step === costs.length-2) {
    return stepCost;
  }

  return stepCost + Math.min(minCostFrom(step+1, costs), minCostFrom(step+2, costs));
}

var minCostClimbingStairs = function(cost) {
  M = Array(cost.length).fill(-1);

  for(let step = cost.length-1; step >= 0; --step) {
    M[step] = minCostFrom(step, cost);
  }

  return Math.min(M[0], M[1]);
};