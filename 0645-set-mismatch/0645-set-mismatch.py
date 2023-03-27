class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        ans = set()
        i = 0
        
        while i < length:
            swap_idx = nums[i] - 1
            at_i = nums[swap_idx]
            
            if at_i == nums[i] and i+1 != nums[i]:
                ans.add(nums[i])
                i+=1
            elif nums[i] == i+1:
                i+=1
            else:
                nums[i],nums[swap_idx] = nums[swap_idx],nums[i]
        i,ans = 0, list(ans)
        while i < length:
            if i+1 != nums[i]:
                ans.append(i+1)
            i+=1
            
        return (ans)
        