class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
    
        def rec(n,k):
            
            if(n == 1):
                return 0
            
            mid = math.ceil(k / 2)
         
            val = rec(n-1, mid)
            
            if(val == 0):
                if(k % 2 == 1):
                    return 0
                else:
                    return 1
        
            else:
                if(k % 2 == 1):
                    return 1
                else:
                    return 0
        return rec(n,k)
            
        