class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}
        
        def dp(idx, length):
            if (idx,length) not in memo:
                if length > n:
                    return 0

                if length == n:
                    return 1
                
                cnt = 0
                for i in range(idx, 5):
                    ans = dp(i, length+1)
                    cnt+=ans
                memo[(idx, length)] = cnt
            
            return memo[(idx,length)]
        
        return dp(0,0)

                
            
            
            
            
            
            
            