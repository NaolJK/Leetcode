class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isPossible(speed):
            tot = 0
            for pile in piles:
                hr = ceil(pile/speed)
                tot+=hr
           
            return (tot) <= h
        
        left,right = 1, max(piles)
        
    
        while right > left:
            middle = (right+left)//2
            
            if isPossible(middle):
                
                right = middle
            else:
                
                left = middle+1
                
        return left