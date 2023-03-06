class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isPossible(n):
            cnt = 0
            for num in citations:
                if num >= n:
                    cnt+=1
            return cnt >= n
        
        left, right = -1,max(citations)+1
    
        while left+1 < right:
            middle = (left+right)//2
            
            if isPossible(middle):
                left = middle
            else:
                right = middle
                
        return left
            
        