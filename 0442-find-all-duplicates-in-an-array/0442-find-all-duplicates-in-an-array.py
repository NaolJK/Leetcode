class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = set()
        
        i = 0
        while i < length:
            swap_idx = nums[i]-1
            num_at_pos = nums[swap_idx]
            if num_at_pos == nums[i] and i+1 != nums[i]:
                ans.add(nums[i])
                i+=1
            elif nums[i] == i+1:
                i+=1
            else:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                
                
        return ans 
        