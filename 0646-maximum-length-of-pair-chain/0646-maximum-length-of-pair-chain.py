class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        length = len(pairs)
        
        dp = [1]*length
        
        pairs.sort(key=lambda x:x[0])
        for i in range(length):
            
            for j in range(i):
                
                # print(pairs[i], pairs[j])
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
        print(dp)
        return max(dp)
                
                
        