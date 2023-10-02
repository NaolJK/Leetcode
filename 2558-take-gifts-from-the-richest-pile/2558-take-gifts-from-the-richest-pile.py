class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        s = []
        heapify(s)
        
        for g in gifts:
            heappush(s, -1*g)
        
        while k > 0:
            r = -1*heappop(s)
            sq = floor(pow(r, 0.5))
            heappush(s, -1*sq)
            k-=1
            
        ans =0
        
        while s:
            r = -1*heappop(s)
            ans+=r
        
        return ans
        