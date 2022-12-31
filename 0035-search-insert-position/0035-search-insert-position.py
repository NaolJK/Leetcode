class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for idx,num in enumerate(nums):
            if target <= num:
                return idx
        
        return len(nums)
        