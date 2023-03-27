class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        length = len(nums)
        
        while i < length:
            if nums[i] < 1:
                i+=1
                continue
                
            swap_idx = nums[i] - 1
            
            if swap_idx >= length:
                i+=1
                continue
            
            at_i = nums[swap_idx]
            
            
            if nums[i] == at_i or i+1 == nums[i]:
                i+=1
            else:
                # print("here", at_i,nums[i])
                nums[i], nums[swap_idx] = nums[swap_idx],nums[i]
                
        # print(nums)
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
            
        return nums[-1] + 1
            
            
        