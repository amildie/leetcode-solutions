// https://leetcode.com/problems/longest-common-prefix/

class Solution {
public:
  string longestCommonPrefix(vector<string>& strs) {
    
    // Empty vector check
    if(strs.empty()) {
      return "";
    }

    // If there is a common prefix it can be, at most,
    // as long as the shortest string. Also, if there
    // is an empty string on strs, the longest common
    // prefix is "".
    int minLength = numeric_limits<int>::max();
    for(auto &str : strs) {
      if(str.length() < minLength) {
        minLength = str.length();
      }
      if(minLength == 0) {
        return "";
      }
    }

    std::string res = "";
    for(int i = 0; i < minLength; ++i) {
      char currentChar = strs[0][i];
      
      // Is the i-nth character the same on all strings?
      bool isPrefix = true;
      for(auto &str : strs) {
        if(str[i] != currentChar) {
          isPrefix = false;
        }
      }
    
      if(isPrefix) {
        res += currentChar;
      } else {
        break;
      }
    }

    return res;
  }
  
};