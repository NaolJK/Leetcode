class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        dp = [1]*length
        
        for i in range(length):
            
            for j in range(i):
                
                if nums[i] > nums[j]:
                    # print("j" , nums[j],"i",nums[i], end = " ")
                    # print()
                    dp[i] = max(dp[i], 1 + dp[j])
            # print()
        
        # print(dp)
        
        return max(dp)