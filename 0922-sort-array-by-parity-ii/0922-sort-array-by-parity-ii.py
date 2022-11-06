class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        odd = 1
        even = 0
        
        for num in nums:
            if num %2 == 0:
                result[even] = num
                even+=2
            else:
                result[odd] = num
                odd+=2
        return result
        
        
            
            
        
                