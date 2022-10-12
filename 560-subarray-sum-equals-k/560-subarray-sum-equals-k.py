class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0
        frequency = {0:1}
        
        for num in nums:
            prefix += num
            
            if prefix-k in frequency:
                result = result + frequency[prefix-k]
                
            if prefix in frequency:
                frequency[prefix]+=1
            else:
                frequency[prefix] = 1
        return result
        
        
        