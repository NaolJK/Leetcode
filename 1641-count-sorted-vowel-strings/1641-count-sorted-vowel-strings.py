class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0]*(n+1) for k in range(5)]
        for x in range(5):
            dp[x][n] = 1
        
        for idx in range(4, -1 , -1):
            for length in range(n-1, -1 , -1):
                cnt = 0
                for i in range(idx,5):
                    cnt+=dp[i][length+1]
                dp[idx][length] = cnt   
                
        return dp[0][0]

                
            
            
            
            
            
            
            