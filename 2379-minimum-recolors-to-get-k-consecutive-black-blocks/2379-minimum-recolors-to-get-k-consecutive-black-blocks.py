class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        cnt = 0
        
        mnm = inf
        
        left = 0
        
        for right in range(len(blocks)):
            
            if blocks[right] == 'W':
                cnt+=1
            
            while left <= right and (right - left + 1) > k:
                
                if blocks[left] == 'W':
                    cnt-=1
                    
                left+=1
            
            if right - left + 1 == k:
                
                mnm = min(cnt, mnm)
        
        return mnm
        