class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left,right = 0,0
        count = 1
        length = len(arr)
        if length == 1:
            return count
        
        while right < length:
            while left+1 < length and arr[left] == arr[left+1]:
                left+=1
            
            while right+1 < length and (arr[right-1] > arr[right] < arr[right+1] or arr[right-1] < arr[right] > arr[right+1]):
                right+=1
            
            count = max(count ,right-left+1)
            left = right
            right+=1
        return (count)
      
            
        
            
                    
                    
    
                    
                
                    
                    
                
                
            
            
        