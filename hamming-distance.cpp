// https://leetcode.com/problems/hamming-distance/

class Solution {
  public:
    int hammingDistance(int x, int y) {  
      unsigned int hamming = 0;
      const unsigned int MAX_LENGTH = 32;

      std::string x_b = std::bitset<MAX_LENGTH>(x).to_string();
      std::string y_b = std::bitset<MAX_LENGTH>(y).to_string();
      
      for(int i = 0; i < MAX_LENGTH; ++i) {
        if(x_b[i] != y_b[i]) hamming++;
      }

      return hamming;
    }
};
