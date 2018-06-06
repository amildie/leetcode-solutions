// https://leetcode.com/problems/nim-game/

class Solution {
public:
    bool canWinNim(int n) {
      // The person whose turn has a k*4 number of stones loses.
      if (n%4 == 0) {
        return false;
      }
      return true;
    }
};