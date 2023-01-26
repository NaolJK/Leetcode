class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        length = len(nums)
        if len(nums) == 1:
            return 1
        count = 0
        while left <= right:
            i = nums[left-1]
            
            while left <= right and nums[left] == i:
                count+=1
                nums[left] = "_"
                left+=1
            left+=1
        left = 0  
        right = 1
        while right < length:
            if nums[left] == "_":
                while right < length and nums[right] == "_":
                    right+=1
                    
                if right < length:
                    nums[left], nums[right] = nums[right],nums[left]
                    
            left+=1
            right+=1
                
        return length - count
        
        
            
        