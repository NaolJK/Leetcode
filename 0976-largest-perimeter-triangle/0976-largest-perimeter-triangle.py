class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        nums_len = len(nums) - 1
        side = nums_len - 2
        long_side  = nums_len
        maximum_perimeter = 0
        
        while side >= 0:
            two_sides_sum = nums[side] + nums[side+1]
            
            if two_sides_sum > nums[long_side]:
                triangle_perimeter = two_sides_sum + nums[long_side]
                maximum_perimeter = max(maximum_perimeter,triangle_perimeter)
                long_side-=1
                side-=1
            long_side-=1
            side-=1
        return maximum_perimeter
    