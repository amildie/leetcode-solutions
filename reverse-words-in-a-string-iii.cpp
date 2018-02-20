// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
  public:
    string reverseWords(string s) {
      vector<string> words;
      stringstream ss(s);
      string item, resp;

      while(getline(ss, item, ' '))
      {
        words.push_back(item);
      }

      for(int i = 0; i < words.size(); ++i)
      {
        if (i > 0) 
        {
          resp.append(" ");
        }
        reverse(words[i].begin(), words[i].end());
        resp.append(words[i]);
      }

      return resp;
    }
};
