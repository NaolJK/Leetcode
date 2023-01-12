class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = left+1
        length = len(nums)
        
        while right < length:
            if nums[left] == 0 and nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
            elif nums[left] == nums[right] and nums[right] == 0:
                right+=1
            else:
                right+=1
                left+=1
            
                
        