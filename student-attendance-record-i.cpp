// https://leetcode.com/problems/student-attendance-record-i/

class Solution {
  public:
    bool checkRecord(string s) {
      int aCount = 0;
      for(int i = 0; i < s.length(); ++i)
      {
        if(s[i] == 'A') aCount++;
      }
      return (aCount < 2 && (s.find("LLL") == string::npos));
    }
};
