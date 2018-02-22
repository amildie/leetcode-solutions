// https://leetcode.com/problems/detect-capital/

class Solution {
  public:
    bool detectCapitalUse(string word) {
      bool allCaps = true;
      bool allLower = true;
      bool onlyFirstCap = true;

      for(int i = 0; i < word.length(); ++i)
      {
        if(isupper(static_cast<int>(word[i])))
        {
          allLower = false;
          if(i > 0)
          {
            onlyFirstCap = false;    
          }
        }
        if(islower(static_cast<int>(word[i])))
        {
          allCaps = false;
        }
      }

      return (allCaps || allLower || onlyFirstCap);
    }
};
