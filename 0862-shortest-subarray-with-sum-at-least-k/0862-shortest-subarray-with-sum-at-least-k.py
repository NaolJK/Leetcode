class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        # prefix = [*list(accumulate(nums))]
        
        
        queue = deque([(0, 0)])
        
        minimum_window = len(nums) + 1
        summation = 0
        left = 0
        for right,n in enumerate(nums):
            summation += n 
            
            while queue and summation - queue[0][1] >= k:
                idx , neg = queue.popleft()
                minimum_window = min(minimum_window, right - idx + 1)
            
            while queue and queue[-1][1] >= summation:
                queue.pop()
            
            queue.append((right+1,summation))
        
        if minimum_window > len(nums):
            minimum_window = -1
        
        return minimum_window
                
            
            
        
    
        
            
            
            
            
            