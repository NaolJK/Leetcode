class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {

       

        int sz = cost.size();
        vector <int> dp(sz, -1);

        function <int(int)> minCost;

        minCost = [&](int i){
            if(i >= sz){
                return 0;
            }
            if(dp[i] == -1){
                int f = minCost(i+1) + cost[i];
                int s = minCost(i+2) + cost[i];
                dp[i] = min(f, s);
;            }
            return dp[i];            
        };
        return min(minCost(0), minCost(1));
    }
};