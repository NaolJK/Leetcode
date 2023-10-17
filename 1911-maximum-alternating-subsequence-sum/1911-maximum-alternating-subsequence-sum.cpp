class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        
        long long mxm_even = 0;
        long long mxm_odd = 0;
        
        for(auto num : nums){
            mxm_even = max(mxm_even, mxm_odd + num);
            mxm_odd = max(mxm_odd, mxm_even - num);
        }
        
        return max(mxm_even, mxm_odd);
    }
};