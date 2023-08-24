class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        target = len(set(nums))
        
        count = 0
        for i in range(len(nums)):
            
            elem = set()
            for j in range(i,len(nums)):
                elem.add(nums[j])
                if len(elem) == target:
                    count+=1
                    
        return count
                    
                
        