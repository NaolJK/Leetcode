class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
    
        def backtrack(i,candidate):
            
            if i >= len(num) and len(candidate) > 2:
                return True
            
            for j in range(i,len(num)):
                
                current_num = num[i:j+1]
                
                if len(current_num) >= 2 and current_num[0] == "0":
                    continue
                if len(candidate) < 2 or (candidate[-1] + candidate[-2]) == int(current_num):
                    candidate.append(int(current_num))
                    ans = backtrack(j+1,candidate)
                    if ans:
                        return True
                    candidate.pop()
                    
                    
        return backtrack(0,[])
        
                    
                
                