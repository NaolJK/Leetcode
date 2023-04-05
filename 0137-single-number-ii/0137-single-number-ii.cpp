class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int count;
        int ans = 0;
        
        for(int i = 0; i<= 31; ++ i){
            count = 0;
            int check = (1 << i);
            for (auto &n : nums){
                if(n & check) ++count;
            }
            if(count % 3){
                ans|=(1<<i);
            }
        }
        return ans;
    }
};