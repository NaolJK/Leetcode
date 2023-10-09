class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int last = upper_bound(nums.begin(), nums.end(), target) - nums.begin();
        int start = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        
        if(start < nums.size() && nums[start] == target){
            return {start, last-1};
        }
        
    
        return {-1,-1};
    }
};