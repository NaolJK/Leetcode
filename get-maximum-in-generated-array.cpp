class Solution {
public:
    int getMaximumGenerated(int n) {
        int max = 0;
        
        vector <int> nums;
        function <int(int, vector<int>&)> mxm;

        mxm = [&](int k, vector<int>& dp){
            if(k ==0 || k ==1) return k;

            if(dp[k] != -1) return dp[k];

            if(k % 2) return dp[k] = mxm(k / 2, dp) + mxm((k / 2) + 1, dp);

            return dp[k] = mxm(k/2, dp);
        };


        int maximum = -1;
        vector <int> dp(n+1, -1);
        for(int i=0; i <= n ; ++i){
            int mx = mxm(i, dp);
            if(mx > maximum) maximum = mx;
        }

        return maximum;
    }
};