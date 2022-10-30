class Solution:
    
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        maxFreq = 0
        nums.sort()
        
        left_window = 0
        right_window = 0
        Sum = 0
        while right_window < len(nums):
            Sum += nums[right_window]
            while nums[right_window] * (right_window - left_window + 1) > Sum + k: 
                Sum -= nums[left_window]
                left_window += 1
            
            maxFreq = max(maxFreq, right_window - left_window + 1)
            right_window  += 1
            
        return maxFreq
            
            
        
                    
                    
                
            
        