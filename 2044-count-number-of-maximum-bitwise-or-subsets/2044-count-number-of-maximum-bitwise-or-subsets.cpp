class Solution {
    int ans=0;
    void backtrack(vector<int> nums,int candidate, int idx, int maximum){
        if(candidate == maximum){
            ++ans;
        }
        
        for (int j= idx; j < nums.size(); ++j){
            backtrack(nums, candidate|nums[j], j+1, maximum);
        }
    }
    
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int maximum = 0;
        
        for (auto &n:nums){
            maximum = maximum | n;
        }
        
        backtrack(nums,0,0,maximum);
        return ans;
    }
};