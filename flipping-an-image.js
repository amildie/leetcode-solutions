// https://leetcode.com/problems/flipping-an-image/

/**
* @param {number[][]} A
* @return {number[][]}
*/
var flipAndInvertImage = function(A) {
  for(let row of A) {
    row = row.reverse();
    for(let i = 0; i < row.length; ++i) {
      row[i] = row[i] ? 0 : 1;
    }
  }
  return A;
};