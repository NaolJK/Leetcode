class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        left = cnt = 0
        
        count = defaultdict(int)
        
        for right in range(len(s)):
            
            count[s[right]]+=1
            
            while left <= right and (count['a'] and  count['b'] and count['c']):
                count[s[left]] -= 1
                left+=1
                
            cnt+=(left)
       
               
        return cnt
            
            
                
            
            
        
        
        
        