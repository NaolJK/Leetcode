class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        
        queue = deque()
        
        for right in range(len(nums)):
            
            if queue and queue[0] < right - k + 1:
                queue.popleft()
            
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            
            queue.append(right)
            
            if right >= k-1:
                # print(k, queue)
                ans.append(nums[queue[0]])
        
        return ans
            
            
            
        