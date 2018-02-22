// https://leetcode.com/problems/length-of-last-word/

class Solution {
  public:
    int lengthOfLastWord(string s) {
      stringstream ss(s);
      string word;

      int count = 0;
      while (ss >> word)
      {
        count = word.length();
      }

      return count;
    }
};
