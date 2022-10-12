class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        left_pointer = 0
        
        while left_pointer < len(nums):
            total-=nums[left_pointer]
            
            if total == left_sum:
                return left_pointer
            left_sum += nums[left_pointer]
            left_pointer +=1
            
        return -1
        