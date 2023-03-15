class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        
        def partitionSum(target):
            total, count = 0, 1 
            for n in nums:
                if total + n > target:
                    count+=1
                    total = 0
                total += n 
                
            return count
        
        while left <= right:
            mid = (left + right) //2 
            res = partitionSum(mid)
            
            if res <= k:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
            
            
         
        
                    
                
                
            