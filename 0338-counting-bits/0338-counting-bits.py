class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        i = 0
        while i < n+1:
            count = 0
            j = i
            while j> 0:
                count += (j& 1)
                j >>= 1
            ans.append(count)
            i+=1
            
        return ans
        