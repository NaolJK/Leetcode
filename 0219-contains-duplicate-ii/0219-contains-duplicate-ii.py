class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left,right = 0,0
        
        exist = set()
        
        while right < len(nums):
            
            window = right - left
            
            
            if window > k:
                exist.remove(nums[left])
                left+=1
                
            if nums[right] in exist and left!=right:
                return True
            
            else:
                exist.add(nums[right])
                right+=1
                
        return False
                
                
                
            
    
        