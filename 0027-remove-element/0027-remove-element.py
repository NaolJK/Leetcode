class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        last_pointer = len(nums) - 1 
        first_pointer = 0
        
        while first_pointer <= last_pointer:
            if nums[first_pointer] == val:
                if nums[first_pointer] == nums[last_pointer]:
                    # nums[last_pointer] = 0
                    last_pointer-=1
                    nums.pop()
                    continue
                else:
                    # nums[first_pointer] = 0
                    
                    # print(nums)
                    nums[first_pointer],nums[last_pointer] = nums[last_pointer], nums[first_pointer]
                    nums.pop()
                    first_pointer+=1
                    last_pointer-=1
            else:
                first_pointer+=1
        # return nums
                