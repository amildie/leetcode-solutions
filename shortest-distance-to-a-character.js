// https://leetcode.com/problems/shortest-distance-to-a-character/

/**
 * @param {string} S
 * @param {character} C
 * @return {number[]}
 */
var shortestToChar = function(S, C) {
  let resp = [];
  for(let i = 0; i < S.length; ++i) {
    
    let distL = 0; 
    let foundL = false;
    for(let j = i; j > -1; --j) {
      if(S[j] === C) {
        foundL = true;
        break;
      }
      distL++;
    }

    let distR = 0; 
    let foundR = false;
    for(let j = i; j < S.length; ++j) {
      if(S[j] === C) {
        foundR = true;
        break;
      }  
      distR++;
    }
    
    if(foundL) {
      if(foundR) {
        resp.push(Math.min(distL, distR)); 
      } else {
        resp.push(distL);    
      }  
    } else {
      resp.push(distR);
    }
    
  }
  return resp;
};