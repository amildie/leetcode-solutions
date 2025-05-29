// https://leetcode.com/problems/count-asterisks

/**
 * @param {string} s
 * @return {number}
 */
var countAsterisks = function(s) {
    let count = 0;
    let pairOpen = true;
    for (i = 0; i < s.length; ++i) {
        if(s[i] === "|") {
            pairOpen = !pairOpen;
        }
        if(s[i] === "*" && pairOpen) {
            count++;
        }
    }
    return count;
};
