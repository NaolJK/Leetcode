class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int sz = cost.size();
        
        vector <int> dp(sz+1, 0);
        
        dp[0] = cost[0];
        dp[1] = cost[1];
        
        for(int i = 2; i <= sz; ++i){
            dp[i] = min(dp[i-1], dp[i-2]);
            if(i != sz) dp[i]+=cost[i];
        }
        
        // for(auto el : dp){
        //     cout << el << " ";
        // }
        return dp[sz];
        
    }
};