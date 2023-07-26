class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        
        long long length = questions.size();
        
        vector<long long> dp(length, 0);
        
        dp[length-1] = questions[length-1][0];
        
        for (int i = length-2; i >= 0 ; --i){
            dp[i] = questions[i][0];
            long long s = questions[i][1];
            
            if(i + s + 1 < length){
                dp[i]+= dp[i + s +1];
            }
            
            dp[i] = max(dp[i], dp[i+1]);
        }
        
        return dp[0];
    }
};