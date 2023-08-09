class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -1*nums[i]
        heapq.heapify(nums)
        a = -1*heapq.heappop(nums)
        b = -1*heapq.heappop(nums)
        
        # print(a, b)
        return ((a) - 1) * ((b) - 1)
        
        
        