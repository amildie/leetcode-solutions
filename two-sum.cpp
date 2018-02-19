// https://leetcode.com/problems/two-sum/

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {
      vector<int> resp;

      for(int i = 0; i < nums.size(); ++i) {
        for(int j = 0; j < nums.size() && j != i; ++j){ 
          if(nums[i] + nums[j] == target) {
            resp.push_back(j);
            resp.push_back(i);
          }
        }
      }

      return resp;
    }
};
