class Solution {
public:
    int tribonacci(int n) {
        vector<int> dp(n+1, -1);

        function <int(int)> tri;
        tri = [&](int n){
            if(n <= 0) return 0;
            if(n == 1 || n == 2) return 1;
            
            if(dp[n] == -1){
                dp[n] = tri(n-1) + tri(n-2) + tri(n-3);
            }
            return dp[n];
        };

        return tri(n);
    }
};