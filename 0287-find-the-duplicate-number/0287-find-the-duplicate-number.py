class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        
        i = 0
        while i < length:
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            nums[abs(nums[i])]*=-1
            i+=1
        
            
            
        