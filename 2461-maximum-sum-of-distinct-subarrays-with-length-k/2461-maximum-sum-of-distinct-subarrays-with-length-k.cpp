class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        
        int left =0; long long ans = 0;
        long long sm = 0;
        unordered_map<int, int> count;
        
        for(int right=0; right < nums.size(); ++right){
            
            ++count[nums[right]];
            sm+=nums[right];
            
            while(right < left || count[nums[right]] > 1){
                sm-=nums[left];
                --count[nums[left]];
                ++left;
            }
            
            if(right - left + 1 == k){
                ans = max(sm , ans);
                sm-=nums[left];
                --count[nums[left]];
                ++left;
            }
        }
        
        return ans;
    }
};