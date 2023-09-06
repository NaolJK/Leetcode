class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        dp = [1]*length
        
        for i in range(length):
            
            for j in range(i):
                
                if nums[i] > nums[j]:
                    
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # print(dp)
        
        return max(dp)