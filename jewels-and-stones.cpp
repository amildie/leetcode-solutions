class Solution {
  public:
    int numJewelsInStones(string J, string S) {
      unsigned int count = 0;
      char jMap[1000];
      memset(jMap, 0, sizeof(jMap));

      for(int i = 0; i < J.length(); ++i)
      {
        jMap[static_cast<int>(J[i])] = 1;
      }

      for(int i = 0; i < S.length(); ++i)
      {
        if (jMap[static_cast<int>(S[i])] == 1) {
          count++;
        }
      }

      return count;
    }
};
