class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #left pointer
        left = 0 
        #right pointer
        right = left+1
        length = len(nums)
        
        while right < length:
            
            #check if the left pointer is equals right pointer 
            if nums[left] == 0 and nums[right] != 0:
                #if they are equal swap them
                nums[left],nums[right] = nums[right],nums[left]
            #check if left pointer is zero and right one is zero and increase right by one 
            elif nums[left] == nums[right] and nums[right] == 0:
                right+=1
            else:
                right+=1
                left+=1
            
                
        