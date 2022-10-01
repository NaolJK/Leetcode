class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0 
        i =0 
        j = len(height)-1
        
        while i < j:
            minimum_val = min(height[i], height[j])
            area = minimum_val * (j-i)
            maximum = max(maximum,area)
            
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        
        return maximum
                    
        