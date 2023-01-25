class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #1 2 3 4   5
        right = 46400
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
            
            
        