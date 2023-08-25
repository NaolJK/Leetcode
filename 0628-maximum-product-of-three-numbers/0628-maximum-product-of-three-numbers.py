class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        p1 = p2 = p3 = -inf
        
        for num in nums:
            
            if num > p1:
                p3 = p2
                p2 = p1
                p1 = num
                
            elif num > p2:
                p3 = p2
                p2 = num
                
                
            elif num > p3:
                p3 = num
                
        n1 = n2 = inf
        
        for num in nums:
            
            if num < n1:
                n2 = n1
                n1 = num
             
                
            elif num < n2:
                n2 = num
                
        # print(p1, p2, p3)
        mx1 = p1 * p2 * p3
        mx2 = n1 * n2 * p1
       
        
        if mx1 != -inf and mx2 != inf:
            return max(mx1, mx2)
        
        if mx1 != -inf:
            return mx1
        
        if mx2 != inf:
            return mx2
        
        
        
        
        

            
        
        
       
                
        
        
        
        
        
        
        