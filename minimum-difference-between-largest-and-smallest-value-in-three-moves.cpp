class Solution {
public:
    int minDifference(vector<int>& nums) {
        if(nums.size() <= 4) return 0;
        
        sort(nums.begin(), nums.end());
        int n = nums.size();

        int mn1 =nums[n - 4] - nums[0]; 
        int mn2 = nums[n - 1] - nums[3];
        int mn3 = nums[n - 3] - nums[1];
        int mn4 = nums[n - 2] - nums[2];

        
        return min({mn1, mn2, mn3, mn4});
    }
};