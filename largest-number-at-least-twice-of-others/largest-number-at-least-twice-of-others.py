class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        bigger = 0 
        next_bigger = -1
        index = 0
        
        for idx,num in enumerate(nums):
            if num > bigger:
                next_bigger = bigger 
                bigger = num
                index = idx
            elif num > next_bigger:
                next_bigger = num
                
                    
        
        twice = 2 * next_bigger         
        if twice <= bigger:
            return index 
        
        return -1
                
        