class Solution {
public:
    int recursive(int i,vector<vector<int>>& dp, vector<int> &coins,int n, int amount){
        if(i == 0){

            if(amount % coins[i] == 0) return amount/coins[i];

            else return 1e9;
        }

        if(dp[i][amount] != -1) return dp[i][amount];

        int notTake = recursive(i-1 ,dp,  coins , n , amount);

        int take = INT_MAX;


        if(coins[i] <= amount){

            take = 1 + recursive(i,dp, coins, n, amount - coins[i]);
        }

        dp[i][amount] = min(take, notTake);

        return dp[i][amount];
    }
    
    int coinChange(vector<int>& coins, int amount) {

        int n = coins.size();

        vector<vector<int>> dp(n, vector<int>(10000,-1));

        int res = recursive(n-1 ,dp, coins , n, amount);

       
        if(res >= 1e9) return -1;

        else return res;
    }
};