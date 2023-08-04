class Solution {
public:
    long long maxArrayValue(vector<int>& nums) {
        long long sm=0, ans=0;
        
        
        for(int i= nums.size()-1; i >=0 ; --i){
            if(nums[i] > sm){
                sm = 0;
            }
            
            sm+=nums[i]; 
            ans = max(ans, sm);
        }
        
        return ans;
    }
};