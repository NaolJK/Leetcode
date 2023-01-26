class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left , right = 0 , len(nums)-1
        op = 0
        while left < right:
            tot = nums[left] + nums[right]
            if tot == k:
                left+=1
                right-=1
                op+=1
            elif tot > k:
                right-=1
            else:
                left+=1
        return op
                
                
        