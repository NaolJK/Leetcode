class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        ans1 = True
        ans2 = True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                ans1 = False
                break
        
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                continue
            else:
                ans2 = False
                break
        
        return ans1 or ans2
        