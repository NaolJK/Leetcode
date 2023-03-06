class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isPossible(n):
            ans = 0
            curr = 0
            for r,num in enumerate(weights):
                if curr+num > n:
                    # print(num,r,curr)
                    ans+=1
                    curr = 0   
                curr+=num
            ans+=1
            return ans <= days
                    
                
        l,r = max(weights),sum(weights)
        
        a = 0
        while l < r:
            mid = (l+r)//2
            # print(isPossible(mid))
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
        
        return r
                