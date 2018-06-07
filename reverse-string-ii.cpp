// https://leetcode.com/problems/reverse-string-ii/

class Solution {
public:
  string reverseStr(string s, int k) {
    for(auto it = s.begin(); it <= s.end(); it += 2*k) {       
      if(it + k <= s.end()) {
        reverse(it, it+k);
      } else {
        reverse(it, s.end());
        break;
      }
    }
    return s;        
  }
};