class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for idx,num in enumerate(nums):
            if idx != num:
                return idx
        
        return len(nums)
        
            
            
            
        