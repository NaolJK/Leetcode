class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int count = 0; 
        for (int i=0; i < nums.size(); ++i){
            int gcd = nums[i];
            if(gcd == k){
             ++count;
            }
            for (int j=i+1; j < nums.size(); ++ j){
                if(gcd % k != 0){
                    break;
                }
                gcd = __gcd(gcd,nums[j]);
                if(gcd == k){
                    ++count;
                }
                
            }
        }
        
        return count;
    }
};