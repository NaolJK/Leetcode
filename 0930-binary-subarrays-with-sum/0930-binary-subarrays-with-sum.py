class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atleastk(k):
            left = 0
            res = 0
            count = 0
            for right in range(len(nums)):
                res+=nums[right]
                
                while left <= right and res > k:
                    res-=nums[left]
                    left+=1
                count+=(right-left+1)
            return count
        ans = abs(atleastk(goal) - atleastk(goal-1))
        return ans
                
                
            