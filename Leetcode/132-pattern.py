class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        max_of_min = -inf
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < max_of_min:
                return True
            
            while stack and stack[-1] < nums[i]:
                elem = stack.pop()
                max_of_min = max(elem,max_of_min)
            
            stack.append(nums[i])
        return False