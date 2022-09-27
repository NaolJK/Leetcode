class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        if c[0] %2 != 0:
            return []
        t=c[0]
        c[0] = 0
        ans = [0] * (t//2)
        
        for x in sorted(c.keys()):
            if c[2*x] >= c[x]:
                t=c[x]
                c[x] -=t
                c[2*x]-=t
                ans+=[x] * t
            else:
                return []
        return ans
                
       
        