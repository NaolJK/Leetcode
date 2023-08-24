class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        
        
        
       
        function<int(int k)> al = [&](int k){
          int left = 0;
          long long sm = 0;
          int cnt = 0;
          for(int right = 0; right < nums.size(); right++){
            sm += nums[right];
              
            while(left <= right && sm > k){
                sm-=nums[left];
                ++left;
            }
            
            cnt+=(right - left + 1);
          }  
        return cnt;
        };
        
        
        return abs(al(goal) - al(goal -1));
    }
};