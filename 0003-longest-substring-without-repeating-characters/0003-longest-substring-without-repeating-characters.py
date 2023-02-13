class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        left = 0
        right = 0
        maximum_gap = 0
        
        while right < len(s):
            if d[s[right]] < 1:
                d[s[right]]+=1
                maximum_gap = max(maximum_gap,right-left+1)
            else:
                d[s[right]]+=1
                while left <= right and d[s[right]]> 1:
                    d[s[left]]-=1
                    left+=1
            right+=1
                      
        return(maximum_gap)
        
                
            
                
                
        