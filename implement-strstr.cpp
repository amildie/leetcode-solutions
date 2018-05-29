// https://leetcode.com/problems/implement-strstr/

class Solution {
public:
  int strStr(std::string haystack, std::string needle) {
    
    // Edge cases  
    if(needle == "") return 0;
    if(haystack == "") return -1;

    for(int i = 0; i < haystack.length(); ++i) {
      int position = i;
      if(needleStartsHere(haystack, needle, position)) {
        return position;
      }
    }

    return -1;
  }

  int needleStartsHere(std::string haystack, std::string needle, int position) {
    for(int i = 0; i < needle.length(); ++i) {
      if(position + i == haystack.length()) {
        return false;
      }    

      if(haystack[position+i] != needle[i]) {
        return false;
      }
    }
    return true;
  }
};