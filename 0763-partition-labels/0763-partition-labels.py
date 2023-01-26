class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for idx,lett in enumerate(s):
            last_idx[lett] = idx
            
        left = 0 
        br = 0
        res =[]
        for i,lett in enumerate(s):
            br = max(br,last_idx[lett])
            
            if i == br:
                res.append(i-left+1)
                left = i+1
                
        return res
                
            
            
            
                
    
        