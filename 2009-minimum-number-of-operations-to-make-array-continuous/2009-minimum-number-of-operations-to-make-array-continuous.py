class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        p_l = len(nums)
        nums.sort()
        
        nums = list(set(nums))
        nums.sort()
        ans = inf
       
        for i in range(len(nums)):
            number = nums[i] + (p_l - 1)
            
            pos = bisect_right(nums, number)
       
            op = pos - i
           
            ans = min(ans, p_l - op)
            
        return ans