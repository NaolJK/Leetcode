class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(candidate,lastnum):
            
            if lastnum != "" and int(candidate) == int(lastnum) - 1:
                return True
            
            for idx in range(1,len(candidate)):
                current_num = candidate[:idx]
                
                if lastnum == "" or int(current_num) == int(lastnum)-1:
                    ans = backtrack(candidate[idx:],current_num)
                    if ans:
                        return True
            return False
        return backtrack(s,"")
        