class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low_pointer = middle_pointer = 0
        high_pointer = len(nums) - 1
        
        while middle_pointer <= high_pointer:
            if nums[middle_pointer] == 0:
                nums[low_pointer], nums[middle_pointer] = nums[middle_pointer], nums[low_pointer]
                low_pointer+=1
                middle_pointer+=1
            elif nums[middle_pointer] == 1:
                middle_pointer+=1
            
            else:
                nums[middle_pointer], nums[high_pointer] = nums[high_pointer], nums[middle_pointer]
                high_pointer -=1
            
                
        
        
        
    
            
            