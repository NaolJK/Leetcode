class Solution:
    def integerBreak(self, n: int) -> int:

        memo = {}
        def dp(currSum):
            if currSum == n:
                return 1

            if currSum > n:
                return 0
            
            if currSum in memo:
                return memo[currSum]

            if currSum in memo:

                return memo[currSum]

            val = 0
            for i in range(1, n):
                
                val = max(val, dp(currSum + i) * i)

            memo[currSum] = val

            return memo[currSum]
        
        return dp(0)
        





        