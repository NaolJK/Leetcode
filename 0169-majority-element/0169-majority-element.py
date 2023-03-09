class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if count == 0:
                c = nums[i]
            if c == nums[i]:
                count+=1
            else:
                count-=1
        return c
        