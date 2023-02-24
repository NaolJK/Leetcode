class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        length = (len(nums)*2)
        stack = []
        
        for i in range(length):
            
            while len(stack) and stack[-1][0] < nums[i%len(nums)]:
                el,idx = stack.pop()
                ans[idx] = nums[i%len(nums)]
            stack.append((nums[i%len(nums)],i%len(nums)))
            
        return (ans)
        