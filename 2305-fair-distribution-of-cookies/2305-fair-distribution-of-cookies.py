class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0]*k
        self.ans = inf
        cookies.sort(reverse=True)
        
        def backtrack(i):
            if i >= len(cookies):
                maximum = max(distribution[::])
                self.ans = min(self.ans,maximum)
                return 
            
            if self.ans <= max(distribution):
                return 
            
            
            for j in range(k):
                distribution[j]+=cookies[i]
                backtrack(i+1)
                distribution[j]-=cookies[i]
                
        backtrack(0)
        return (self.ans)
                

        