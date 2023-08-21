class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        left = ans = 0
        
        count = defaultdict(int)
        sm = 0
        for right in range(len(nums)):
            
            count[nums[right]] += 1
            sm+=nums[right]
            
            # print(right, count)
            
            while left < right and count[nums[right]] > 1:
                sm-=nums[left]
                count[nums[left]] -= 1
                
                left+=1
                
               
                
            if (right - left + 1) == k:
                # print(right, left)
                ans = max(ans, sm)
                sm-=nums[left]
                count[nums[left]]-=1
                left+=1
                
       
                
        return ans
                
            
            
            
            
                
        
        
        
        
            
            
            
        
        
            
            
            
            
        
        