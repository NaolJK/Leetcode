class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        #first create two pointers
        #check if the slow pointer is zero or not
            #if it is zero check the fast pointer if zero or non zero
                 #if the fast pointer is zero move it to the next and check again
                 #if the fast pointer is non zero swap with the slow one
                    
            #if the slow pointer is non zero move both to the next
        
        length = len(nums) - 1
        i = 0
        j = 1
        
        while j <= length:
            if nums[i] == 0:
                if nums[j] == 0:
                    j+=1
                else:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i+=1
                    j+=1
            else:
                j+=1
                i+=1
                    
                    
        