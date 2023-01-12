class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        left_pointer = 0
        right_pointer = left_pointer + 1
        length = len(nums)
        
        while right_pointer < length:
            if nums[left_pointer] == nums[right_pointer]:
                nums[left_pointer]*=2
                nums[right_pointer]*=0
            right_pointer+=1
            left_pointer+=1

        left_pointer = 0
        right_pointer = left_pointer + 1
        while right_pointer < length:
            if nums[left_pointer] == 0 and nums[right_pointer] != 0:
                nums[left_pointer],nums[right_pointer] = nums[right_pointer],nums[left_pointer]
            elif nums[left_pointer] == nums[right_pointer] and nums[left_pointer] == 0:
                right_pointer+=1
            else:
                right_pointer+=1
                left_pointer+=1
        return nums
        