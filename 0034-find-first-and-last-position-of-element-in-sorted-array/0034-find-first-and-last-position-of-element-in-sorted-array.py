class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums,target)
        second = bisect_right(nums,target) -1
        
        # print(first,second)
        if first >= len(nums) or second >= len(nums):
            return [-1, -1]
        elif nums[first] != target or nums[second] != target:
            return [-1,-1]
        
        return [first,second]
        