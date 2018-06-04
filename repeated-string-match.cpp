// https://leetcode.com/problems/repeated-string-match/

class Solution {
public:
  int repeatedStringMatch(string A, string B) {
    
    string temp = A;
    int repetitions = 1;
    int MAX_SIZE = 10000;

    while(A.length() < B.length()) {
      A += temp;
      repetitions++;
    }

    if(A.find(B) != string::npos) {
      return repetitions;
    }

    while(A.length() <= MAX_SIZE) {
      A += temp;
      repetitions++;
      if(A.find(B) != string::npos) {
        return repetitions;
      }
    }

    return -1;
  }
};