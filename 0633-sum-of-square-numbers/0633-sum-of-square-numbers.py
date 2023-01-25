class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(c**0.5)
        left = 0
        
        while left <= right:
            ans = (left*left) + (right*right)
            if ans == c:
                return True
            elif ans > c:
                right-=1
            else:
                left+=1
        
        print(left,right)
            
                
        return False
            
            
        