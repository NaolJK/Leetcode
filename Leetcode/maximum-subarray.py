class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = -inf
        currsum = 0
        
        for num in nums:
            currsum = max(currsum + num, num)
            ans = max(ans, currsum)
            
        return ans
       
        
        