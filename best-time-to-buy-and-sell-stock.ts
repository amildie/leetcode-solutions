// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

function maxProfit(prices: number[]): number {
  let min = Number.POSITIVE_INFINITY;
  let max = Number.NEGATIVE_INFINITY;
   
  for(let i = 0; i < prices.length; ++i) {
    min = prices[i] < min ? prices[i] : min;
    max = prices[i] - min > max ? prices[i] - min : max;
  }

  return max;
};