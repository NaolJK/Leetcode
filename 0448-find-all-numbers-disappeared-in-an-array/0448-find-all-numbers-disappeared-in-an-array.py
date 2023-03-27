class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        
        i = 0
        while i < length:
            num_at_i = nums[(nums[i]%length)-1]
            swap_idx = (nums[i]%length)-1
            if num_at_i == nums[i] or i + 1 == nums[i]:
                i+=1
            else:
                nums[i], nums[swap_idx] = nums[swap_idx],nums[i]
        i = 0
        
        while i < length:
            if i+1 != nums[i]:
                ans.append(i+1)
            i+=1
        return ans
                
            
            