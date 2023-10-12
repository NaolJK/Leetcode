class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        mnm = nums[0]
        
        for n in nums:
            mnm&=n
        
        if mnm > 0:
            return 1
        
        cnt = 0
        c = nums[0]
        for i in range(len(nums)):
            c&=nums[i]
            
            if c == mnm:
                cnt+=1
                if i + 1 < len(nums):
                    c = nums[i+1]
            

        return cnt
        