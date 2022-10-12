class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_zero = 1
        left_window = 0 
        ans = 0
        
        
        for right_window in range(len(nums)):
            if nums[right_window] == 0:
                max_zero-=1
            
            while max_zero < 0 and left_window <= right_window:
                if nums[left_window] == 0:
                    max_zero+=1
                    
                left_window += 1
                
            ans = max(ans,right_window-left_window)
        
        return ans
                    
        